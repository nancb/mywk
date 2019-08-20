from datetime import datetime

from dao import BaseDao
from libs.crypt import check_password
from logger import api_logger

class UserDao(BaseDao):
    #保存用户
    def save(self, **values):
        api_logger.info('db insert wklc_users: <%s>' % values['userTel'])
        return super(UserDao, self).save('wklc_users', **values)
    def query_accounts(self,user_id):
        sql = 'select id from wklc_users ' \
              'where userTel=%s'
        user_accounts = self.query(sql,user_id)  # 返回用户对象
        return user_accounts
    def save2(self, **values):
        # api_logger.info('db insert wklc_accounts: <%s>' % values['user_id'])
        return super(UserDao, self).save('wklc_accounts', **values)

    # 检查手机号是否已存在
    def check_login_name(self,userTel):
        result = self.query('select id as cnt from wklc_users where userTel=%s', userTel)
        return not bool(result)
    #用户登录信息
    def login(self, userTel, password):#输入用户名密码
        sql = 'select id, password from wklc_users ' \
              'where userTel=%s'
        user_data = self.query(sql, userTel)#返回用户对象

        if user_data:
            #得到用户id和密码
            user_id, auth_str = (user_data[0].get('id'),
                                 user_data[0].get('password'))
             #验证用户名密码是否正确
            print(user_id)
            if check_password(password,auth_str):
                # 验证成功获取详细信息
                user_profile = self.get_profile(user_id)
                if user_profile is None:
                    return {
                        'user_id': user_id,
                        'userTel': userTel
                    }
                #返回用户详细信息
                return user_profile
            api_logger.warn('用户 %s 的口令不正确' %  userTel)
            raise Exception('用户 %s 的口令不正确' %  userTel)
        else:
            api_logger.warn('查无此用户 %s' %  userTel)
            raise Exception('查无此用户 %s' % userTel)

    def get_profile(self, user_id):
        # 获取用户的详细信息
        sql = "select * from wklc_lendrecords " \
              "where user_id=%s"
        user_lendrecords = self.query(sql, user_id)
        data=[
           {"tit":"月账户","num":0},#月
           {"tit":"季账户", "num": 0},  #季
           {"tit":"年账户", "num": 0},  # 年
           {"tit":"特供账户", "num": 0},  # 特殊
           {"tit":"虚拟账户", "num": 0},
           {"tit":"昨日期望收益","num":0},
           {"tit":"累计期望回报","num":0}

        ]

        if user_lendrecords:

            for lendrecord in user_lendrecords:
                if str(lendrecord['product_id']).startswith('902'):
                    product = self.query_product(lendrecord['product_id'])
                    productRate = product['productRate']
                    productCloseTime = product['productCloseTime']
                    lendMoney = lendrecord['lendMoney']
                    lendTime = lendrecord['lendTime']
                    yesr = float(lendMoney)*float(productRate)/36500 #平均明天收
                    if (lendTime.toordinal()+productCloseTime)>datetime.now().toordinal():
                        ljsu = (datetime.now().toordinal() - lendTime.toordinal()) * yesr
                    else:
                        ljsu = productCloseTime*yesr
                        if lendrecord['product_id']==9022:
                            lendMoney = 0
                    tomony = lendMoney+ljsu
                    data[5]["num"]=float('%.2f'%(data[5]["num"]+yesr))
                    data[6]["num"]=float('%.2f'%(data[6]["num"]+ljsu))
                    data[0]["num"]=float('%.2f'%(data[0]["num"]+tomony))

                if str(lendrecord['product_id']).startswith('903'):
                    product = self.query_product(lendrecord['product_id'])
                    productRate = product['productRate']
                    productCloseTime = product['productCloseTime']
                    lendMoney = lendrecord['lendMoney']
                    lendTime = lendrecord['lendTime']
                    yesr = float(lendMoney)*float(productRate)/36500
                    if lendTime.toordinal()+productCloseTime>datetime.now().toordinal():
                        ljsu = (datetime.now().toordinal() - lendTime.toordinal()) * yesr
                    else:

                        ljsu = productCloseTime*yesr
                    tomony = lendMoney+ljsu
                    data[5]["num"] = float('%.2f' % (data[5]["num"] + yesr))
                    data[6]["num"] = float('%.2f' % (data[6]["num"]+ljsu))
                    data[1]["num"]=float('%.2f'%(data[1]["num"]+tomony))

                if str(lendrecord['product_id']).startswith('904'):
                    product = self.query_product(lendrecord['product_id'])
                    productRate = product['productRate']
                    productCloseTime = product['productCloseTime']
                    lendMoney = lendrecord['lendMoney']
                    lendTime = lendrecord['lendTime']
                    yesr = float(lendMoney)*float(productRate)/36500
                    if lendTime.toordinal()+productCloseTime>datetime.now().toordinal():
                        ljsu = (datetime.now().toordinal() - lendTime.toordinal()) * yesr
                    else:
                        ljsu = productCloseTime*yesr
                    tomony = lendMoney+ljsu
                    data[5]["num"] = float('%.2f' % (data[5]["num"] + yesr))
                    data[6]["num"] = float('%.2f' % (data[6]["num"]+ljsu))
                    data[2]["num"]=float('%.2f'%(data[2]["num"]+tomony))


                if str(lendrecord['product_id']).startswith('901'):
                    product = self.query_product(lendrecord['product_id'])
                    productRate = product['productRate']
                    productCloseTime = product['productCloseTime']
                    lendMoney = lendrecord['lendMoney']
                    lendTime = lendrecord['lendTime']
                    yesr = float(lendMoney)*float(productRate)/36500
                    if lendTime.toordinal()+productCloseTime>datetime.now().toordinal():
                        ljsu = (datetime.now().toordinal() - lendTime.toordinal()) * yesr
                    else:
                        ljsu = productCloseTime*yesr
                    tomony = lendMoney+ljsu
                    data[5]["num"] = float('%.2f' % (data[5]["num"] + yesr))
                    data[6]["num"] = float('%.2f' % (data[6]["num"]+ljsu))
                    data[3]["num"]=float('%.2f'%(data[3]["num"]+tomony))
        self. update_accounts(data[0]["num"],data[1]["num"],data[2]["num"],data[3]["num"],user_id)
        return data


    #查询产品
    def query_product(self,productId):
        sql = 'select * from wklc_products ' \
              'where productId=%s'
        user_data = self.query(sql, productId)  # 返回用户对象
        return user_data[0]
    #保存出借记录
    def lend_save2(self,**values):

        return super(UserDao, self).save('wklc_lendrecords', **values)
    #更新用户账户
    def update_accounts(self,monthAccount,sensonAccount,yearAccount,specialAccount,user_id):
        sql = "update wklc_accounts set monthAccount=%s," \
              "sensonAccount=%s,yearAccount=%s," \
              "specialAccount=%s where user_id=%s"
        resful = self.update(sql,monthAccount,sensonAccount,yearAccount,specialAccount,user_id)
        return resful


     #查询原密码
    def select_pwd(self, id):
        sql = 'select password from wklc_users where id = %s'
        pwd = self.query(sql, id)
        print(pwd[0])
        return pwd[0]
    #更新密码
    def update_pwd(self, password, id):
        sql = 'update wklc_users set password = %s where id = %s'
        resful = self.update(sql, password, id)
        return resful

    #查询所有的用户id
    def query_idlist(self):
        sql = 'select id from wklc_users'
        id_list = self.query(sql)  # 返回用户对象
        return id_list

    #保存上传图像的key
    # def update_pwd(self, img_key, id):
    #     sql = 'update wklc_users set img_key = %s where id = %s'
    #     resful = self.update(sql,img_key, id)
    #     return resful
    def update_user(self,totalMoney,yersterdayReturn,totalReturn,user_id):
        sql = 'update wklc_users set totalMoney=%s,yersterdayReturn=%s,totalReturn=%s where id=%s'
        result = self.update(sql,totalMoney,yersterdayReturn,totalReturn,user_id)
        return result








if __name__ == '__main__':
    dao = UserDao()
    # dao.login('disen', 'disen666')  # 登录成功之后的数据
    print(dao.check_login_name('disen'))