from __future__ import absolute_import, unicode_literals

import redis
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


import random

from flask import jsonify

from libs import rd


def new_code(phone):
    """
    获取验证码
    :param phone:
    :return:
    """
    code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    print(phone,code)
    # 保存到cache
    rd.set(phone,code)
    # 发送验证给用户
    send_sms_code(phone, code)


def confirm(phone, input_code):
    # 从缓存cache中读取phone对应的验证码
    # 和input_code进行比较，如果通过则返回True
    # print(rd.get(phone))
    # print(rd.get(phone).decode())
    try:
        if rd.get(phone).decode() == input_code:
            return True
        else:
            return False
    except:
        return False

#绑定银行可发送验证码
def new_phone_code(phone):
    code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    print(phone, code)
    # 保存到cache
    phone1 = "*" + phone
    rd.set(phone1, code)
    # 发送验证给用户
    send_sms_code(phone, code)

#绑定银行卡
def confirm_code(phone, input_code):
    try:
        phone1 = "*" + phone
        if rd.get(phone1).decode() == input_code:
            return True
        else:
            return False
    except:
        return False


def send_sms_code(phone, code):
    # coding=utf-8

    client = AcsClient('LTAIRiQGIywYBeYN', 'ZOHiNBYPr72dCFog2fLU5Pu9RvVAIf', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "Disen工作室")
    request.add_query_param('TemplateCode', "SMS_128646125")
    request.add_query_param('TemplateParam', '{"code":"%s"}' % code)

    response = client. do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))


if __name__ == '__main__':

    new_code('13409515204')