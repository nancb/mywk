from flask import Blueprint, jsonify, request

from dao.verify_dao import Verify_Dao
from libs.cache import get_token_user_id
from logger import api_logger
verify_blue = Blueprint('verify_blue',__name__)

dao = Verify_Dao()
#查询是否认证
@verify_blue.route('/verify/',methods = ['POST'])
def rzlend():
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
    if all((req_data.get('token', False),)):
        token=req_data.get('token')
        user_id = get_token_user_id(token)
        if dao.user_verify(user_id):
            return jsonify({
            "code":200,
            "msg":"已认证"
            })
        else:
            return jsonify({
            "code": 201,
            "msg": "未认证"
            })
    return jsonify({
        "code": 203,
        "msg": "未获得token"
    })
#实名认证
@verify_blue.route('/to_verify/',methods = ['POST'])
def to_rzlend():
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
    if all((req_data.get('userName', False),
            req_data.get('userCard', False),
            req_data.get('token',False))):
        userName = req_data['userName']
        userCard = req_data["userCard"]
        token = req_data['token']
        data={}
        data['user_id'] = get_token_user_id(token)
        if dao.toverify(userName,userCard):
            data['verify_id']= dao.toverify(userName,userCard)['id']
            if not dao.query_user_verify(data['verify_id']):
                if dao.save_verify(**data):
                    print(data['user_id'])
                    if dao.update_user(data['user_id']):
                        return jsonify({
                            'code': 200,
                            'msg': "姓名和身份证号,对上了"
                        })
                else:
                    return jsonify({
                        'code': 201,
                        'msg': "认证失败"
                    })
            else:
                return jsonify({
                    'code': 202,
                    'msg': "此卡已被绑定"
                })

        else:
            return jsonify({
                'code':203,
                'msg':"请输入正确的姓名和身份证号"
            })
    else:
        return jsonify({
            'code':204,
            'msg': "传入参数不足"
        })



