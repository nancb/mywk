from flask import Blueprint, request,jsonify

from dao.carts_dao import CartDao
from libs import cache

dao = CartDao()
blue_cart = Blueprint('cart_api',__name__)

@blue_cart.route('/add_goods/',methods=('POST',))  #添加商品
def add_goods():
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
        req_data['checked'] = 0
        goods_id = req_data.get('goods_id')

        cart = dao.check_login_name(user_id,goods_id)

        if cart:
            req_data['cart_goods_num'] = 1
            print("******",req_data)
            dao.save(**req_data)
            return jsonify({
                'code': 200,
                'msg': '添加商品成功'
            })
        else:
            goods = dao.check_cart(user_id,goods_id)
            goods_num = int(goods['cart_goods_num'])
            goods_num += 1
            dao.update_goods_num(user_id,goods_id,goods_num)
            return jsonify({
                'code':200,
                'msg':'添加商品成功'
            })
    else:
        return jsonify({"msg":"token值错误或者过期，请先登录"})

@blue_cart.route('/reduce_goods/',methods=('POST',)) #减少商品
def reduce_goods():
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
        goods_id = req_data.get('goods_id')

        cart = dao.check_login_name(user_id,goods_id)

        if cart:
            return jsonify({
                'code': 203,
                'msg': '请先添加商品！'
            })
        else:
            goods = dao.check_cart(user_id,goods_id)
            goods_num = int(goods['cart_goods_num'])
            if goods_num > 0:
                goods_num -= 1
                print(goods_num)
                dao.update_goods_num(user_id,goods_id,goods_num)
                return jsonify({
                    'code':200,
                    'msg':'删除商品成功'
                })
            else:
                dao.del_goods(user_id,goods_id)
                return jsonify({
                    'code':202,
                    'msg':'商品已经删除到0，删除该商品记录'
                })
    else:
        return jsonify({"msg":"token值错误或者过期，请先登录"})

@blue_cart.route('/show_cart/',methods=('POST','GET'))  #展示购物车
def place_order():
    token = request.args.get('token', None)
    if token is None:
        return jsonify({
            'code': 202,
            'msg': '没有登录，请先登录'
        })
    if bool(cache.check_token(token)):
        total_kf = 0
        user_id = cache.get_token_user_id(token)
        carts_lists = dao.show_cars(user_id)
        for cart in carts_lists:
            data1 = {}
            goods_id = cart['goods_id']
            goods = dao.show_sort(goods_id)
            data1['goodsId'] = goods['goodsId']
            data1['goodsName'] = goods['goodsName']
            data1['littlePic'] = goods['littlePic']
            data1['kfCoin'] = goods['kfCoin']
            cart['goods'] = data1
            if cart['checked'] == 1:
                kf = goods['kfCoin']
                total_kf += kf*cart['cart_goods_num']
            else:
                pass
        return jsonify({
            'code':200,
            'msg':'购物车详情为',
            'goods_list':carts_lists,
            'totel':total_kf
        })
    else:
        return jsonify({"msg":"token值错误或者过期，请先登录"})

@blue_cart.route('/pitch_good/',methods=('GET',)) #改变商品选中状态
def pitch_good():
    token = request.args.get('token', None)
    if token is None:
        return jsonify({
            'code': 202,
            'msg': '没有登录，请先登录'
        })
    if bool(cache.check_token(token)):
        user_id = cache.get_token_user_id(token)
        good_id = request.args.get('goods_id')
        checked = int(request.args.get('checked'))
        if checked == 'true':
            checked = 1
            checked_update = dao.update_goods_checked(user_id,good_id,checked)
        else:
            checked = 0
            checked_update = dao.update_goods_checked(user_id,good_id,checked)
        if checked_update:
            return jsonify({
                'code':200,
                'msg':'商品修改状态成功'
                })
    else:
        return jsonify({"msg":"token值错误或者过期，请先登录"})

@blue_cart.route('/del_goods/',methods=('POST',)) #删除选中商品
def del_good():

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
        goods_id = req_data['goods_id']
        resulte = dao.del_goods(user_id,goods_id)
        if resulte:
            return jsonify({
                'code':200,
                'msg':'删除已选中商品'
            })
        else:
            return jsonify({
                'code':202,
                'msg':'删除商品由于某种原因删除失败'
            })
    else:
        return jsonify({"msg":"token值错误或者过期，请先登录"})