from flask import Blueprint, jsonify, request

from dao.order_dao import OrderDao
from libs import cache

dao = OrderDao()
blue_order = Blueprint('order_api',__name__)



@blue_order.route('/add_order/',methods=('POST',))  #添加订单
def add_order():
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
        print()
        user_id = cache.get_token_user_id(token)
        kfCion_totel = req_data['kfCoin']
        users = dao.check_user(user_id)
        print(users)
        if int(users['userKfCoin']) < kfCion_totel:
            return jsonify({
                'code':202,
                'msg':'空粉币不足不能下单'
            })
        else:
            req_data['totalfuZuan'] = 0
            req_data['totalkfCoin'] = kfCion_totel
            req_data['pay'] = 0
            req_data['user_id'] = user_id
            req_data.pop('token')
            req_data.pop('kfCoin')
            print(req_data)
            order_list = dao.save(**req_data)

        if order_list:
            del_carts = dao.query_checked(user_id)
            if del_carts:
                return jsonify({
                    'code': 200,
                    'msg': '下单成功~'
                })
        else:
            return jsonify({
                'code':303,
                'msg':'由于莫种原因 ，下单失败'
            })
    else:
        return jsonify({"msg":"token值错误或者过期，请先登录"})

@blue_order.route('/pay_order/',methods=('POST',)) #支付订单
def payOrder():
    req_data = None
    if request.headers['Content-Type'].startswith('application/json'):
        req_data = request.get_json()
    print(req_data)
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
        data = {}
        user_id = cache.get_token_user_id(token)
        user_oder = dao.cheak_order(user_id)
        user = dao.check_user(user_id)
        payCoin = user_oder['totalkfCoin']
        userCoin = user['userKfCoin']
        if userCoin > payCoin:
            surplusCoin = userCoin - payCoin
            resulte = dao.surplus_Coin(user_id,surplusCoin)
            data['userName'] = req_data['userName']
            data['userPhone'] = req_data['userPhone']
            data['address'] = req_data['address']
            data['detailAddress'] = req_data['detailAddress']
            data['postalCode'] = req_data['postalCode']
            data['order_id'] = req_data['order_id']
            if resulte:
                add_save = dao.save_add(**data)
                if add_save:
                    return jsonify({
                        'code': 200,
                        'msg': '下单成功'
                    })
                else:
                    return jsonify({
                        'code': 303,
                        'msg': '获取未知错误，地址保存有误'
                    })
            if resulte:
                return jsonify({
                    'code':200,
                    'msg':'下单成功'
                })
            else:
                return jsonify({
                    'code':303,
                    'msg':'获取未知错误，下单失败'
                })
        else:
            return jsonify({
                'code': 202,
                'msg': '空粉币不足，不能下单'
            })
    else:
        return jsonify({"msg":"token值错误或者过期，请先登录"})

@blue_order.route('/show_oder/',methods=('GET',)) #展示订单
def show_order():
    token = request.args.get('token', None)
    if token is None:
        return jsonify({
            'code': 202,
            'msg': '没有登录，请先登录'
        })
    if bool(cache.check_token(token)):
        user_id = cache.get_token_user_id(token)
        orders = dao.query_order(user_id)
        default_address = dao.query_default(user_id)
        return jsonify({
            'code':200,
            'orders':orders,
            'default_address':default_address
        })
    else:
        return jsonify({"msg":"token值错误或者过期，请先登录"})

@blue_order.route('/show_oderinfo/',methods=('GET',)) #展示订单详情
def show_orderinfo():
    token = request.args.get('token', None)
    print(token)
    if token is None:
        return jsonify({
            'code': 202,
            'msg': '没有登录，请先登录'
        })
    if bool(cache.check_token(token)):
        order_id = request.args.get('order_id')
        orders_info = dao.query_order_info(order_id)
        add_detail = dao.query_address(order_id)
        for goods in orders_info:
            goods_id = goods['goods_id']
            goods_detail = dao.show_goods(goods_id)
            goodsDetails = goods_detail['goodsDetails']
            goodsDescribe = goods_detail['goodsDescribe']
            goodsSpecification = goods_detail['goodsSpecification']
            g = goodsDetails.split(',')
            d = goodsDescribe.split('；')
            a = goodsSpecification.split('；')
            goods_detail['goodsDetails'] = g
            goods_detail['goodsDescribe'] = d
            goods_detail['goodsSpecification'] = a
            goods['detail'] = goods_detail
        return jsonify({
            'code':200,
            'msg':'展示订单详情商品',
            'goods':orders_info,
            'address':add_detail
        })
    else:
        return jsonify({"msg":"token值错误或者过期，请先登录"})

@blue_order.route('/save_address/',methods=('POST',))
def save_address():
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
        req_data.pop('token')
        req_data['user_id'] = user_id
        order_add = dao.select_add(user_id)
        if order_add:
            save_add = dao.wklc_default_address(**req_data)
            if save_add:
                return jsonify({
                    'code':200,
                    'msg':'储存地址成功'
                })
            else:
                return jsonify({
                    'code': 300,
                    'msg': '储存地址失败'
                })
        else:
            del_old_add = dao.del_add(user_id)
            if del_old_add:
                save_new_add = dao.wklc_default_address(**req_data)
                if save_new_add:
                    return jsonify({
                        'code':200,
                        'msg':'储存地址成功'
                    })
                else:
                    return jsonify({
                        'code':300,
                        'msg':'储存地址失败'
                    })
            else:
                return jsonify({
                    'code': 300,
                    'msg': '储存地址失败'
                })
    else:
        return jsonify({"msg":"token值错误或者过期，请先登录"})



