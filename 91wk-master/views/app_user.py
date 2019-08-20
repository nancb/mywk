import os
import uuid
from datetime import datetime

from flask import Blueprint
from flask import request, jsonify
from werkzeug.datastructures import FileStorage

from dao.user_dao import UserDao
from libs import cache, oss
from libs.cache import get_token_user_id
from libs.crypt import make_password, check_password
from libs.sms import confirm, new_code
from logger import api_logger


blue = Blueprint('user_api', __name__)
dao = UserDao()
@blue.route('/check_tel/', methods=('GET', ))
def check_login_name():
    # 查询参为数
    userTel = request.args.get('userTel')
    result = {
        'code': 200,
        'msg': '用户名不存在'
    }

    if not UserDao().check_login_name(userTel):
        result['code'] = 300
        result['msg'] = '用户名已存在'
    else:
        new_code(userTel)

    return jsonify(result)
@blue.route('/regist/', methods=('POST',))
def user_regist():
    # 前端请求的Content-Type: application/json
    req_data = None
    api_logger.info(request.headers)
    if request.headers['Content-Type'].startswith('application/json'):
        req_data = request.get_json()

    if req_data is None:
        api_logger.warn('%s 请求参数未上传-json' % request.remote_addr)
        return jsonify({
            'code': 9000,
            'msg': '请上传json数据，且参数必须按api接口标准给定'
        })
    api_logger.debug(req_data)
    # 验证上传的必须的数据是否存在
    if all((req_data.get('userTel', False),
            req_data.get('password', False),
            req_data.get('code', False))):
        input_code = req_data.get('code')
        phone = req_data.get('userTel')
        password = req_data.get('password')
        if dao.check_login_name(phone):
            if confirm(phone, input_code):
                req_data['password']=make_password(req_data.get('password'))
                req_data['userName']=req_data['userTel'][:3]+"******"+req_data['userTel'][-3:]
                req_data['userGrade_id'] ='1',
                req_data['totalMoney'] = '0'
                req_data['yersterdayReturn'] ='0'
                req_data['totalReturn'] = '0'
                req_data['userKfCoin'] = '500000'
                req_data['userfuZuan'] = '0'
                req_data['xyMoney'] = '5000'
                req_data['zyMoney'] = '0'
                req_data['is_Verify']='0'
                req_data['userPic']='0'
                req_data.pop('code')
                if dao.save(**req_data):

                    sql = 'select * from wklc_users ' \
                          'where userTel=%s'
                    userTel = req_data['userTel']
                    user_datas = dao.query(sql,userTel)[0]
                    req_data2 = {}
                    req_data2['user_id'] =user_datas['id']
                    req_data2['monthAccount'] = 0
                    req_data2["sensonAccount"] = 0
                    req_data2["yearAccount"] = 0
                    req_data2['specialAccount'] = 0
                    req_data2['virtualPrincipal'] = 0
                    dao.save2(**req_data2)

                    login_user = dao.login(userTel, password)

                    token = cache.new_token()
                    # 用户基本信息
                    sql = 'select * from wklc_users ' \
                          'where userTel=%s'


                    # 将token存在redis的缓存中，绑定的数据可以是用户Id也可以是用户的信息
                    cache.save_token(token, user_datas['id'])
                    #注册成功添加出借50000出借7天
                    data ={}
                    data['user_id']= user_datas['id']
                    data['product_id'] = 9022
                    data['lendUserTel'] = req_data['userName']
                    data['lendTime'] = datetime.now()
                    data['lendMoney'] = 5000
                    dao.lend_save2(**data)
                    money = 0
                    for i in login_user[:-2]:
                        money += i["num"]
                    totalMoney = float('%.2f' % (user_datas['zyMoney'] + money))
                    yersterdayReturn = login_user[5]['num']
                    totalReturn = login_user[6]['num']
                    dao.update_user(totalMoney, yersterdayReturn, totalReturn, user_datas['id'])
                    return jsonify({
                        'code': 200,
                        'token': token,
                        'userTel': user_datas['userTel'],
                        'userGrade_id': user_datas['userGrade_id'],
                        'totalMoney':totalMoney,
                        'zyMoney': user_datas['zyMoney'],
                        'xyMoney': user_datas['xyMoney'],
                        'yersterdayReturn': yersterdayReturn,
                        'totalReturn': totalReturn,
                        'userKfCoin': user_datas['userKfCoin'],
                        'userfuZuan': user_datas['userfuZuan'],
                        'Account': login_user[:-2]
                    })

                else:
                    return jsonify({
                    'code': 300,
                    'msg': '插入数据失败, 可能存在某一些字段没有给定值'
                })
            else:
                return jsonify({
                    'code': 203,
                    'msg': '验证码输入错误'
                })
        else:
            return jsonify({
                'code': 201,
                'msg': '用户名已存在，不能再注册'
            })

    else:
        return jsonify({
            'code': 204,
            'msg': '输入参数不全,参数必须按api接口标准给定'
        })


@blue.route('/login/', methods=('GET',))
def user_login():
    api_logger.debug('user login get action!')
    # 验证参数
    userTel = request.args.get('userTel', None)
    password = request.args.get('password', None)
    if all((bool(userTel), bool(password))):
        dao = UserDao()
        # 获取登录用户的信息
        try:
            login_user = dao.login(userTel, password)
            # 生成token
            token = cache.new_token()
            #用户基本信息
            sql = 'select * from wklc_users ' \
                  'where userTel=%s'
            user_datas = dao.query(sql,userTel)[0]
            # 将token存在redis的缓存中，绑定的数据可以是用户Id也可以是用户的信息
            cache.save_token(token,user_datas['id'])
            user_id  = user_datas['id']
            sql = 'select lendTime from wklc_lendrecords ' \
                  'where user_id=%s and product_id=9022'
            product  = dao.query(sql, user_id)
            if product:
                if product[0]['lendTime'].toordinal()+7<datetime.now().toordinal():
                    user_datas['xyMoney']=0
            money = 0
            for i in login_user[:-2]:
                money+=i["num"]
            totalMoney = float('%.2f' % (user_datas['zyMoney'] + money))
            yersterdayReturn = login_user[5]['num']
            totalReturn = login_user[6]['num']
            dao.update_user(totalMoney, yersterdayReturn, totalReturn, user_id)
            return jsonify({
                'code': 200,
                'token': token,
                'userTel': user_datas['userTel'],
                'userGrade_id':user_datas['userGrade_id'],
                'totalMoney': totalMoney,
                'zyMoney':user_datas['zyMoney'],
                'xyMoney':user_datas['xyMoney'],
                'yersterdayReturn':yersterdayReturn,
                'totalReturn': totalReturn,
                'userKfCoin':user_datas['userKfCoin'],
                'userfuZuan':user_datas['userfuZuan'],
                'Account':login_user[:-2]
            })
        except Exception as e:
            return jsonify({
                'code': 202,
                'msg':str(e)
            })
    else:
        return jsonify({
            'code': 101,
            'msg': '请求参数login_name和auth_str必须存在'
        })

#用户刷新
@blue.route('/refresh/', methods=('GET',))
def refresh():
    token = request.args.get('token', None)
    if token:
        user_id = get_token_user_id(token)
        if user_id:
            sql = 'select * from wklc_users ' \
                  'where id=%s'
            user_datas = dao.query(sql,user_id)[0]
            sql = 'select lendTime from wklc_lendrecords ' \
                  'where user_id=%s and product_id=9022'
            product = dao.query(sql, user_id)
            if product:
                if product[0]['lendTime'].toordinal() + 7 < datetime.now().toordinal():
                    user_datas['xyMoney'] = 0
            money = 0
            user_info = dao.get_profile(user_id)
            for i in user_info[:-2]:
                money += i["num"]
            totalMoney= float('%.2f' % (user_datas['zyMoney'] + money))
            yersterdayReturn=user_info[5]['num']
            totalReturn= user_info[6]['num']
            dao.update_user(totalMoney, yersterdayReturn, totalReturn, user_id)
            return jsonify({
                'code': 200,
                'token': token,
                'userTel': user_datas['userTel'],
                'userGrade_id': user_datas['userGrade_id'],
                'totalMoney': totalMoney,
                'zyMoney': user_datas['zyMoney'],
                'xyMoney': user_datas['xyMoney'],
                'yersterdayReturn':yersterdayReturn,
                'totalReturn': totalReturn,
                'userKfCoin': user_datas['userKfCoin'],
                'userfuZuan': user_datas['userfuZuan'],


                'Account': user_info[:-2]
            })

@blue.route('/hello/',methods=('POST','GET'))
def ccc():
    return jsonify({"name":"666"})

#修改用户登录密码
@blue.route('/change_pwd/',methods=('POST',))
def change_pwd():
    req_data = None
    if request.headers['Content-Type'].startswith('application/json'):
        req_data = request.get_json()
    if req_data is None:
        return jsonify({
            'code': 9000,
            'msg': '请上传json数据，且参数必须按api接口标准给定'
        })
    token = req_data.get('token', None)
    if token is None:
        return jsonify({
            'code': 202,
            'msg': '没有登录，请先登录'
        })
    if bool(cache.check_token(token)):
        user_id = cache.get_token_user_id(token)
        pwd = dao.select_pwd(user_id)
        pwd1 = pwd['password']
        oldpwd = req_data['oldpwd']
        newpwd = req_data['newpwd']
        once_newpwd = req_data['once_newpwd']
        if check_password(oldpwd,pwd1):
            if newpwd == once_newpwd:
                m_new_password = make_password(str(newpwd))
                new_password = dao.update_pwd(m_new_password,user_id)
                if new_password:
                    return jsonify({
                        'code':200,
                        'msg':'修改成功'
                    })
            else:
                return jsonify({
                    'code':201,
                    'msg':'两次输入密码不一致'
                })
        else :
            return jsonify({
                'code':202,
                'msg': '原密码错误'
            })
    else:
        return jsonify({"msg":"token值错误或者过期，请先登录"})


#上传用户图像
@blue.route('/upload_avator/', methods=('POST',))
def upload_avator():
    # 上传的头像字段为 img
    # 表单参数： token
    file: FileStorage = request.files.get('img', None)
    token = request.form.get('token', None)

    if all((bool(file), bool(token))):
        # 验证文件的类型, png/jpeg/jpg, 单张不能超过2M
        # content-type: image/png, image/jpeg
        user_id = get_token_user_id(token)
        print(file.content_length, 'bytes')
        if file.content_type in ('image/png',
                                 'image/jpeg',
                                 ):
            filename = uuid.uuid4().hex \
                       + os.path.splitext(file.filename)[-1]
            file.save(filename)

            # 上传到oss云服务器上
            key = oss.upload_file(filename)

            os.remove(filename)  # 删除临时文件

            # 将key写入到DB中
            # dao.update_pwd(key,user_id)
            return jsonify({
                'code': 200,
                'msg': '上传文件成功',
                'file_key': key
            })
        else:
            return jsonify({
                'code': 201,
                'msg': '图片格式只支持png或jpeg'
            })

    return jsonify({
        'code': 100,
        'msg': 'POST请求参数必须有img和token'
    })


@blue.route('/img_url/<string:key>/', methods=('GET', ))
def get_img_url(key):
    img_type = int(request.args.get('type', 0))

    img_url = oss.get_small_url(key) if img_type == 0 else oss.get_small_url(key)
    return jsonify({
        'url': img_url
    })


