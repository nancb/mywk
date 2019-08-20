from flask import Blueprint, jsonify, request

from dao.goods_dao import GoodsDao

bule_goods = Blueprint('goods_api',__name__)

dao = GoodsDao()


@bule_goods.route('/show_goods/',methods=('GET',)) #展示所有商品
def show_order():
    print("****")
    goods_list = dao.show_goods()
    goods_big = dao.show_biggoods()
    for goods in goods_list:
        goodsDetails = goods['goodsDetails']
        goodsDescribe = goods['goodsDescribe']
        goodsSpecification = goods['goodsSpecification']
        g = goodsDetails.split(',')
        d = goodsDescribe.split('；')
        a = goodsSpecification.split('；')
        goods['goodsDetails'] = g
        goods['goodsDescribe'] = d
        goods['goodsSpecification'] = a
    return jsonify({
        'code':200,
        'msg':'商品详情',
        'goods_list':goods_list,
        'goods_big':goods_big
    })

@bule_goods.route('/sort_good/',methods=('GET',)) #点击大类展示大类中的商品
def showbig():
    big_id = request.args.get('big_id')
    big = dao.query_big(big_id)
    titel = big['bigname']
    sort_goods = dao.show_sort(big_id)
    for goods in sort_goods:
        goodsDetails = goods['goodsDetails']
        goodsDescribe = goods['goodsDescribe']
        goodsSpecification = goods['goodsSpecification']
        g = goodsDetails.split(',')
        d = goodsDescribe.split('；')
        a = goodsSpecification.split('；')
        goods['goodsDetails'] = g
        goods['goodsDescribe'] = d
        goods['goodsSpecification'] = a
    return jsonify({
        'code':200,
        'msg':'商品详情',
        'title':titel,
        'sort_goods':sort_goods
    })
