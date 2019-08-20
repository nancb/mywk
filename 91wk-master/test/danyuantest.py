"""
单元测试：
    本次测试了以下8小部分，共测试了36个接口。
"""
import requests
from unittest import TestCase


class AddressTest(TestCase):
    # 一、用户登录注册
    def test_check(self):        # 1.电话号码验证接口
        url = 'http://101.37.252.237:9001/check_tel/?userTel=18163810350'
        resp = requests.get(url=url)
        print(resp.json())

    def test_regist(self):      # 2.用户注册接口
        url = 'http://101.37.252.237:9001/regist/'
        data = {
            'userTel': "17392323163",
            'password': '123456',
            'code':"6758"
        }
        resp = requests.post(url=url, json=data)
        print(resp.json())

    def test_login(self):      # 3.用户登录接口
        url = 'http://101.37.252.237:9001/login/?userTel=17392323163&password=123456'
        resp = requests.get(url=url)
        print(resp.json())

    def test_refresh(self):    # 4.用户刷新页面
        url = 'http://101.37.252.237:9001/refresh/?token=8b1f36f33ac04a04a5cd380a4f0cd23e'
        resp = requests.get(url=url)
        print(resp.json())

    def test_change_pwd(self):   # 5.修改密码接口
        url = 'http://101.37.252.237:9001/change_pwd/'
        data = {
            "token": "8b1f36f33ac04a04a5cd380a4f0cd23e",
            "oldpwd": "9999",
            "newpwd": "123456",
            "once_newpwd": "123456"
        }
        resp = requests.post(url=url, json=data)
        print(resp.json())

    # 二、产品信息接口
    def test_all_pro(self):   # 6.全部的产品信息
        url = 'http://101.37.252.237:9001/all_pro/'
        resp = requests.get(url=url)
        print(resp.json())

    def test_lendrecords(self):  # 7.查询每个产品的出借记录
        url = 'http://101.37.252.237:9001/all_pro/'
        data = {
            'productId':'9012'
        }
        resp = requests.post(url=url,data=data)
        print(resp.json())

    def test_lendinfos(self):  # 8.信息披露
        url = 'http://101.37.252.237:9001/lendinfos/'
        resp = requests.get(url=url)
        print(resp.json())

    def test_verify(self):   # 9.查询用户是否实名认证
        url = 'http://101.37.252.237:9001/verify/'
        data = {"token": "8b1f36f33ac04a04a5cd380a4f0cd23e"}
        resp = requests.post(url=url,json=data)
        print(resp.json())

    def test_to_verify(self):  # 10.用户实名认证
        url = 'http://101.37.252.237:9001/to_verify/'
        data = {
            "token": "8b1f36f33ac04a04a5cd380a4f0cd23e",
            "userName":"张西靖",
            "userCard":"612421199806062000"
            }
        resp = requests.post(url=url,json=data)
        print(resp.json())

    def test_rzcard(self):  # 11.查询用户是否绑卡
        url = 'http://101.37.252.237:9001/rzcard/'
        data = {
            "token": "8b1f36f33ac04a04a5cd380a4f0cd23e"
        }
        resp = requests.post(url=url, json=data)
        print(resp.json())

    def test_send_cardcode(self):  # 12.绑定银行卡业务时发送验证码
        url = 'http://101.37.252.237:9001/send_cardcode/?userTel=17392323163'
        resp = requests.get(url=url)
        print(resp.json())

    def test_to_rzcard(self):  # 13.绑定银行卡业务
        url = 'http://101.37.252.237:9001/to_rzcard/'
        data = {
            "token": "8b1f36f33ac04a04a5cd380a4f0cd23e",
            "cardNum":"6227753378036378767",
            "cardTel":"17392323163",
            "code":"2763",
            "cardPwd":"123456"
        }
        resp = requests.post(url=url, json=data)
        print(resp.json())

    def test_recharge(self):  # 14.充值业务
        url = 'http://101.37.252.237:9001/recharge/'
        data = {
            "token": "8b1f36f33ac04a04a5cd380a4f0cd23e",
            "number":"60",
            "cardPassword":"123456"
        }
        resp = requests.post(url=url, json=data)
        print(resp.json())

    def test_to_lend(self):  # 15.使用自有本金出借业务
        url = 'http://101.37.252.237:9001/to_lend/'
        data = {
            "token": "8b1f36f33ac04a04a5cd380a4f0cd23e",
            "product_id":"9022",
            "lendMoney":"25",
            "lendpassword":"123456",
        }
        resp = requests.post(url=url, json=data)
        print(resp.json())

    def test_to_lend2(self):  # 16.使用银行卡出借
        url = 'http://101.37.252.237:9001/to_lend2/'
        data = {
            "token": "8b1f36f33ac04a04a5cd380a4f0cd23e",
            "product_id":"9022",
            "lendMoney":"250",
            "lendpassword":"123456",
        }
        resp = requests.post(url=url, json=data)
        print(resp.json())

    def test_user_lend(self):   # 17.用户的出借记录
        url = 'http://101.37.252.237:9001/user_lend/?token=8b1f36f33ac04a04a5cd380a4f0cd23e'
        resp = requests.get(url=url)
        print(resp.json())

    # 三、商品模块
    def test_show_goods(self):  # 18.全部的商品信息
        url = 'http://101.37.252.237:9001/show_goods/'
        resp = requests.get(url=url)
        print(resp.json())

    def test_sort_good(self):  # 19.查询每种类型的商品
        url = 'http://localhost:9001/sort_good/?big_id=1002'
        resp = requests.get(url)
        print(resp.json())

    # 四、购物车模块
    def test_add_goods(self):  # 20.添加商品在购物车
        url = 'http://101.37.252.237:9001/add_goods/'
        data = {
            "token": "aad679636fe643a181a03ecb539db9f4",
            "goods_id": 3
        }
        resp = requests.post(url=url, json=data)
        print(resp.json())

    def test_reduce_goods(self):  # 21.减少商品在购物车
        url = 'http://101.37.252.237:9001/reduce_goods/'
        data = {
            "token": "aad679636fe643a181a03ecb539db9f4",
            "goods_id": 2
        }
        resp = requests.post(url, json=data)
        print(resp.json())

    def test_show_cart(self):   # 22.展示购物车
        url = 'http://101.37.252.237:9001/show_cart/?token=aad679636fe643a181a03ecb539db9f4'
        resp = requests.get(url)
        print(resp.json())

    def test_pitch_good(self):   # 23.改变购物车选中状态
        url = 'http://101.37.252.237:9001/pitch_good/?token=f30c207cd06843a6bddbeefe0243bcdf&goods_id='+'2'+'&checked='+'true'
        resp = requests.get(url)
        print(resp.json())

    def test_del_goods(self):   # 24.删除选中的商品
        url = 'http://101.37.252.237:9001/del_goods/'
        data = {
            "token": "aad679636fe643a181a03ecb539db9f4",
            "goods_id": 2
        }
        resp = requests.post(url, json=data)
        print(resp.json())

    def test_all_checked(self):  # 25.全选改变选中状态
        url = 'http://101.37.252.237:9001/all_checked/?token=aad679636fe643a181a03ecb539db9f4&checked=true'
        resp = requests.get(url)
        print(resp.json())

    # 五、订单模块
    def test_add_order(self):   # 26.添加订单到订单列表
        url = 'http://101.37.252.237:9001/add_order/'
        data = {
            "token":"aad679636fe643a181a03ecb539db9f4",
            "kfCoin":2563
        }
        resp = requests.post(url=url, json=data)
        print(resp.json())

    def test_show_oder(self):   # 27.展示支付页面详情
        url = 'http://101.37.252.237:9001/show_oder/?orderNum=2019070500015&token=aad679636fe643a181a03ecb539db9f4'
        resp = requests.get(url=url)
        print(resp.json())

    def test_pay_order(self):   # 28.付款
        url = 'http://101.37.252.237:9001/pay_order/'
        data = {
            "token": "f30c207cd06843a6bddbeefe0243bcdf",
            "orderNum":"2019070500015"
        }
        resp = requests.post(url=url, json=data)
        print(resp.json())

    def test_show_orderinfo(self):   # 29.展示订单详情
        url = 'http://101.37.252.237:9001/show_orderinfo/?orderNum=2019070500015&token=f30c207cd06843a6bddbeefe0243bcdf'
        resp = requests.get(url=url)
        print(resp.json())

    def test_save_address(self):  # 30.添加修改默认地址
        url = 'http://101.37.252.237:9001/save_address/'
        data = {
            "token":"f30c207cd06843a6bddbeefe0243bcdf",
            "userName":"jifan",
            "userPhone":"13400001111",
            "address":"陕西省",
            "detailAddress":"雁塔区QF",
            "postalCode": "11111"
        }
        resp = requests.post(url, json=data)
        print(resp.json())

    def test_my_order(self):   # 31.展示我的所有订单
        url = 'http://101.37.252.237:9001/my_order/?token=f30c207cd06843a6bddbeefe0243bcdf'
        resp = requests.get(url)
        print(resp.json())

    def test_pay_kf(self):   # 32.展现支付页面
        url = 'http://101.37.252.237:9001/pay_kf/?token=f30c207cd06843a6bddbeefe0243bcdf&orderNum=2019070500010'
        resp = requests.get(url=url)
        print(resp.json())

    # 六、会员等级
    def test_members(self):   # 33.会员等级
        url = 'http://101.37.252.237:9001/members/'
        resp = requests.get(url=url)
        print(resp.json())

    # 七、轮播图地址
    def test_bannerinfo(self):   # 34.轮播图
        url = 'http://101.37.252.237:9001/bannerinfo/'
        resp = requests.get(url=url)
        print(resp.json())

    # 八、头像上传
    def test_upload_avator(self):   # 35.上传用户图像
        url = 'http://101.37.252.237:9001/upload_avator/'
        data = {
            "token": "8b1f36f33ac04a04a5cd380a4f0cd23e",
        }
        files = {
            'img': ('aaa.png', open(r'C:\Users\Administrator\Desktop\wk_project\Test\aaa.png', 'rb'), 'image/png'),
        }
        resp = requests.post(url=url, data=data,files=files)
        print(resp.json())

    def test_img_url(self):   # 36.接收图像路由
        url = 'http://101.37.252.237:9001/img_url/ab9bcf56a18b48008f367ac3250b3e1d'
        resp = requests.get(url=url)
        print(resp.json())

