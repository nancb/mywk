from flask import Blueprint, jsonify

from dao.bannerinfo_dao import BannerInfoDao

bannerinfo_blue = Blueprint('bannerinfo_blue',__name__)

dao = BannerInfoDao()
#轮播图
@bannerinfo_blue.route('/bannerinfo/',methods = ['GET','POST'])
def bannerinfo():
    data=dao.show_bannerinfo()
    return jsonify(data)