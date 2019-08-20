from dao import BaseDao


class GoodsDao(BaseDao):
    def show_goods(self):
        sql = 'select * from wklc_goods'
        good_list = self.query(sql)
        return good_list

    def show_biggoods(self):
        sql = 'select * from wklc_goodsinfo'
        goodsinfo = self.query(sql)
        return goodsinfo

    def show_sort(self,big_id):
        sql = 'select * from wklc_goods where big_id=%s'
        good_list = self.query(sql,big_id)
        return good_list

    def query_big(self, id):
        sql = 'select * from wklc_goodsinfo where bigid=%s'
        detail = self.query(sql, id)
        print(detail)
        return detail[0]