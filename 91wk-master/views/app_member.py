from flask import Blueprint, jsonify

from dao.member_dao import MembersDao

members_blue = Blueprint('members_blue',__name__)

dao = MembersDao()
#会员等级
@members_blue.route('/members/',methods = ['GET','POST'])
def members():
    data=dao.show_members()
    return jsonify(data)