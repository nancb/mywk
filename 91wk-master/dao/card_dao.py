from dao import BaseDao
from libs.crypt import make_password


class Card_Dao(BaseDao):
    #查询是否绑定银行卡
    def user_card(self,user_id):
        sql = 'select * from wklc_user_card where user_id=%s'
        user_card = self.query(sql,user_id)
        if user_card:
            return user_card[0]
        else:
            return False
    #绑卡业务
    def tocard(self,cardNum,cardTel):
        sql = 'select * from wklc_cards where cardNum=%s and cardTel=%s'
        card = self.query(sql,cardNum,cardTel)
        if card:
            return card[0]
        else:
            return False
    def query_card(self,card_id):
        sql = 'select * from wklc_cards where id=%s'
        card = self.query(sql,card_id)
        if card:
            return card[0]
        else:
            return False
    def query_user(self,user_id):
        sql = 'select * from wklc_users where id=%s'
        user= self.query(sql,user_id)
        if user:
            return user[0]
        else:
            return False

    def save_card(self, **values):
        return super(Card_Dao, self).save('wklc_user_card', **values)
    def update_card_money(self,zyMoney,card_id):
        sql = 'update wklc_cards set cardMoney=%s where id=%s'
        result = self.update(sql,zyMoney,card_id)
        return result
    def update_user_zymoney(self,zyMoney,user_id):
        sql = 'update wklc_users set zyMoney=%s where id=%s'
        result = self.update(sql,zyMoney,user_id)
        return result
    def update_card_passwod(self,cardPwd,card_id):
        sql = 'update wklc_cards set cardPwd=%s where id=%s'
        result = self.update(sql,cardPwd,card_id)
        return result
    def query_user_card(self,card_id):
        sql = 'select * from wklc_user_card ' \
              'where card_id=%s'
        user_data = self.query(sql,card_id)  # 返回用户对象
        if user_data:
            return user_data[0]
        else:
            return False
