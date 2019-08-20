from datetime import datetime

from flask import Blueprint,request,jsonify

from dao.lend_dao import LendDao
from libs import cache
from libs.cache import get_token_user_id
from libs.crypt import check_password
from logger import api_logger

lend_blue = Blueprint('lend_blue',__name__)
dao = LendDao()

#自有本金出借
@lend_blue.route('/to_lend/',methods=('GET','POST'))
def to_lend():
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
    if all((req_data.get('token', False),
            req_data.get('product_id', False),
            req_data.get('lendMoney', False),
            req_data.get('lendpassword',False))):
        datas={}
        token = req_data.get('token')
        datas['user_id']= get_token_user_id(token)
        datas['product_id'] = req_data.get('product_id')
        datas['lendTime']=datetime.now()
        user=dao.query_user(datas['user_id'])[0]
        datas['lendUserTel']=user['userName']
        datas['lendMoney'] = req_data.get('lendMoney')
        datas['is_past'] = '0'
        user_id = datas['user_id']
        user_cart = dao.query_user_cart(user_id)
        cartid = user_cart['card_id']
        card = dao.query_cart(cartid)
        cardPwd = card['cardPwd']
        lendpassword = req_data.get('lendpassword')
        if check_password(lendpassword,cardPwd):
            if float(datas['lendMoney'])<float(user['zyMoney']):

                if dao.lend_save(**datas):
                    zyMoney = float(user['zyMoney'])-float(datas['lendMoney'])

                    dao.update_user_zymoney(zyMoney,user_id)

                    return jsonify({
                        'code':200,
                        'msg':"成功借出"
                    })
                else:
                    return jsonify({
                        'code': 201,
                        'msg': "出借失败"
                    })
            else:
                return jsonify({
                    'code':203,
                    'msg':'账户余额不足请先充值'
                })
        else:
            return jsonify({
                "code":205,
                "msg":'密码输入错误'
            })

    else:
        return jsonify({
        'code': 204,
        'msg': '输入参数不全,参数必须按api接口标准给定'
        })



#银行卡出借
@lend_blue.route('/to_lend2/',methods=('GET','POST'))
def to_lend2():
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
    if all((req_data.get('token', False),
            req_data.get('product_id', False),
            req_data.get('lendMoney', False),
            req_data.get('lendpassword', False))):
        datas = {}
        token = req_data.get('token')
        datas['user_id'] = get_token_user_id(token)
        datas['product_id'] = req_data.get('product_id')
        datas['lendTime'] = datetime.now()
        user = dao.query_user(datas['user_id'])[0]
        datas['lendUserTel'] = user['userName']
        datas['lendMoney'] = req_data.get('lendMoney')
        datas['is_past']='0'
        user_id = datas['user_id']
        user_cart = dao.query_user_cart(user_id)
        cardid = user_cart['card_id']
        card = dao.query_cart(cardid)
        cardPwd = card['cardPwd']
        lendpassword = req_data.get('lendpassword')

        if check_password(lendpassword, cardPwd):
            if float(datas['lendMoney']) < float(card['cardMoney']):
                if dao.lend_save(**datas):
                    cardMoney = float(card['cardMoney']) - float(datas['lendMoney'])
                    dao.update_user_card(cardMoney,cardid)
                    return jsonify({
                        'code': 200,
                        'msg': "成功借出"
                    })
                else:
                    return jsonify({
                        'code': 201,
                        'msg': "参数可能有误"
                    })
            else:
                return jsonify({
                    'code': 203,
                    'msg': '账户余额不足请先充值'
                })
        else:
            return jsonify({
                "code": 205,
                "msg": '密码输入错误'
            })
    else:
        return jsonify({
            'code': 204,
            'msg': '输入参数不全,参数必须按api接口标准给定'
        })












