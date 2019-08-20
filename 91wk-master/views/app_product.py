import datetime

from flask import Blueprint,request,jsonify

from dao.product_dao import ProductDao

from logger import api_logger

product_blue = Blueprint('product_blue',__name__)
dao = ProductDao()
#全部的产品
@product_blue.route('/all_pro/',methods=('POST','GET'))
def show_pro():
    datas=[]

    all_prouductstyles = dao.all_productstyles()
    for prouductstyle in all_prouductstyles:
        data={}
        data['productBigId'] = prouductstyle['productBigId']
        data['productBigName']=prouductstyle['productBigName']
        all_prouducts=dao.all_products(data['productBigId'])
        data['pruduct_info']=all_prouducts
        datas.append(data)

    return jsonify(datas)
#每种产品的出借记录
@product_blue.route('/lendrecords/',methods=('POST',))
def lendrecords():
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
    if all((req_data.get('productId', False),)):
        all_lendrecords = dao.all_lendrecords(req_data.get('productId'))
        if all_lendrecords:
            datas = []
            for i in all_lendrecords:
                data ={}
                data["lendMoney"] = i["lendMoney"]
                data["lendTime"]=str(i["lendTime"])
                data['lendUserTel']=i['lendUserTel']
                datas.append(data)
            return jsonify(datas)
        else:
            return jsonify({
                'code':202,
                'msg':'没有该出借记录'
            })
    else:
        return jsonify({"code":201,
                        "msg":"产品id输入有误"})

#信息披露
@product_blue.route('/lendinfos/',methods=('GET',))
def lendinfo():
    lends = dao.all_lendInfo()
    return jsonify(lends)

