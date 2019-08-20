from flask import jsonify

from dao import BaseDao
from logger import api_logger

class LendDao(BaseDao):
    def lend_save(self,**values):

        return super(LendDao, self).save('wklc_lendrecords', **values)
    def query_user(self,userid):
        sql = 'select * from wklc_users where id=%s'
        return self.query(sql,userid)
    def update_user_zymoney(self,zyMoney,user_id):
        sql = 'update wklc_users set zyMoney=%s where id=%s'
        result = self.update(sql,zyMoney,user_id)
        return result
    def update_user_card(self,cardMoney,card_id):
        sql = 'update wklc_cards set cardMoney=%s where id=%s'
        result = self.update(sql, cardMoney,card_id)
        return result
    def query_account(self,userid):
        sql = 'select * from wklc_accounts where user_id=%s'
        return self.query(sql, userid)
    # def update_user_account(self,user_id):
    #     sql = 'update wklc_users set  where id=%s'
    #     result = self.update(sql,user_id)
    #     return result
    def query_user_cart(self,userid):
        sql = 'select * from wklc_user_card  where user_id=%s'
        return self.query(sql, userid)[0]
    def query_cart(self,cardid):
        sql = 'select * from wklc_cards  where id=%s'
        return self.query(sql,cardid)[0]