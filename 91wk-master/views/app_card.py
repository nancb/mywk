from flask import Blueprint, jsonify, request

from dao.card_dao import Card_Dao
from libs.cache import get_token_user_id
from libs.crypt import make_password, check_password
from libs.sms import new_phone_code, confirm_code
from logger import api_logger

card_blue = Blueprint('card_blue',__name__)

dao = Card_Dao()
#查询是否绑卡
@card_blue.route('/rzcard/',methods = ['POST'])
def rzcard():
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
        token = str(req_data.get('token'))
        user_id = get_token_user_id(token)
        card = dao.user_card(user_id)
        if card:
            card_id=card['card_id']
            cardNum = dao.query_card(card_id)['cardNum']
            return jsonify({
                "code":200,
                "msg":"已绑卡",
                "cardNum":cardNum
            })
        else:
            return jsonify({
                "code": 201,
                "msg": "未绑定卡"
            })
    else:
        return jsonify({
            "code": 202,
            "msg": "请按接口文件传入相应的值"
        })

#绑卡时发送验证码
@card_blue.route('/send_cardcode/',methods = ['get'])
def sms_set():
    #获取银行卡的手机号
    userTel = request.args.get('userTel')
    if userTel:
        new_phone_code(userTel)
        return jsonify({
            'code':200,
            'msg':'发送验证码成功'
        })
    else:
        return jsonify({
            'code':202,
            'msg':'电话获取失败'
        })

#绑定银行卡业务
@card_blue.route('/to_rzcard/',methods = ['POST'])
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
    if all((req_data.get('cardNum', False),
            req_data.get('cardTel', False),
            req_data.get('cardPwd',False),
            req_data.get('code', False),
            req_data.get('token', False))):
        cardNum = req_data['cardNum']
        cardTel = req_data['cardTel']
        cardPwd = make_password(req_data['cardPwd'])
        code = req_data['code']
        token = req_data['token']
        data={}
        data['user_id'] = get_token_user_id(token)
        # if confirm_code(cardTel,code):
        if dao.tocard(cardNum,cardTel):
            if confirm_code(cardTel, code):
                data['card_id']= dao.tocard(cardNum,cardTel)['id']
                #初始化密码
                dao.update_card_passwod(cardPwd,data['card_id'])
                #建立人卡关系
                if not dao.query_user_card(data['card_id']):
                    if dao.save_card(**data):
                        return jsonify({
                            'code': 200,
                            'msg': "银行卡，绑定成功"
                        })
                    else:
                        return jsonify({
                            'code': 204,
                            'msg': "绑定失败"
                        })
                else:
                    return jsonify({
                        'code': 205,
                        'msg': "此卡已被绑定"
                    })
            else:
                return jsonify({
                    'code': 203,
                    'msg': "验证码错误"
                })
        else:
            return jsonify({
                'code':202,
                'msg':"未找到此卡"
            })

    else:
        return jsonify({
            'code': 201,
            'msg': "请按api接口传入相应的数据"
        })

#充值业务
@card_blue.route('/recharge/',methods = ['POST'])
def recharge():
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
    if all((req_data.get('token', False),
            req_data.get('number', False),
            req_data.get('cardPassword', False))):
        user_id = get_token_user_id(req_data.get('token'))
        if user_id:
            user = dao.query_user(user_id)
            number = req_data['number']
            user_card = dao.user_card(user_id)
            if user_card:
                card_id = user_card["card_id"]
                card = dao.query_card(card_id)
                cardPassword = str(req_data.get('cardPassword'))
                card_pwd = card['cardPwd']
                if check_password(cardPassword, card_pwd):
                    cardMoney =card['cardMoney']
                    number = float(number)
                    if number < cardMoney:
                        cardMoney=card['cardMoney']-number
                        dao.update_card_money(cardMoney,card_id)
                        zyMoney = user['zyMoney']+number
                        dao.update_user_zymoney(zyMoney,user_id)
                        return jsonify({
                            'code':200,
                            'msg':'成功充值%s'%(number)
                        })


                    else:
                        return jsonify({
                           'code':201,
                            'msg':'银行卡中余额不足'
                        })
                else:
                    return jsonify({
                        'code':204,
                        'msg':"支付密码输入错误"
                    })
            else:
                return jsonify({
                    'code':203,
                    'msg':'用户还未绑卡'
                })
        else:
            return jsonify({
                'code':202,
                'msg':'用户未登录'
            })
    else:
        return jsonify({
            'code':201,
            'msg':'传入参数不有误'
        })


