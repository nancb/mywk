from dao import BaseDao


class OrderDao(BaseDao):
    def check_user(self,user_id):
        sql = 'select * from wklc_users where id=%s'
        users = self.query(sql,user_id)
        return users[0]

    def save(self, **values):
        print("******",values)
        return super(OrderDao, self).save('wklc_orders', **values)

    def save_add(self,**values):
        return super(OrderDao,self).save('wklc_address',**values)

    def wklc_default_address(self,**values):
        return super(OrderDao, self).save('wklc_default_address', **values)

    def cheak_order(self,user_id):
        sql = 'select * from wklc_orders where user_id=%s and pay=0'
        orders = self.query(sql,user_id)
        print(orders)
        return orders[0]

    def surplus_Coin(self,user_id,Coin):
        sql = 'update wklc_users set userKfCoin=%s where id=%s'
        resulte = self.update(sql,Coin,user_id)
        print(resulte)
        if resulte:
            order_update = self.order_update(user_id)
            return order_update

    def order_update(self,user_id):
        sql = 'update wklc_orders set pay=1 where user_id=%s'
        resulte = self.update(sql,user_id)
        return resulte

    def delete_carts(self,user_id):
        sql = 'delete from wklc_carts where user_id=%s and checked=1'
        resulte = self.update(sql,user_id)
        return resulte

    def query_checked(self,user_id):
        sql = 'select goods_id,cart_goods_num from wklc_carts where user_id=%s and checked=1'
        goods_id_list = self.query(sql,user_id)
        for goods in goods_id_list:
            goods_id = goods["goods_id"]
            goods_carys_num = goods["cart_goods_num"]
            print(goods)
            print(goods_carys_num)
            sql = 'select urplussNum from wklc_goods where goodsId=%s'
            goods = self.query(sql,goods_id)
            print(goods)
            goods_num = goods[0]['urplussNum']
            print(goods_num)
            redidue = goods_num - goods_carys_num
            print(redidue)
            if redidue > 0:
                sql = 'update wklc_goods set urplussNum=%s where goodsId=%s'
                resulte = self.update(sql,redidue,goods_id)
                if resulte:
                    resulte_del = self.delete_carts(user_id)
                    if resulte_del:
                        sql = 'select id from wklc_orders where user_id=%s and pay=0'
                        orders_id = self.query(sql,user_id)
                        o_id = orders_id[0]['id']
                        if o_id:
                            data = {}
                            data['order_id'] = o_id
                            data['goods_id'] = goods_id
                            data['order_goods_num'] = goods_carys_num
            else:
                raise Exception("商品数量不足，发生错误")
            super(OrderDao, self).save('wklc_orderdetail',**data)
        return True

    def query_order(self,user_id):
        sql = 'select * from wklc_orders where user_id=%s'
        order = self.query(sql,user_id)
        return order

    def query_order_info(self,order_id):
        sql = 'select * from wklc_orderdetail where order_id=%s'
        order_list = self.query(sql,order_id)
        return order_list


    def show_goods(self,id):
        sql = 'select * from wklc_goods where goodsId=%s'
        good_list = self.query(sql,id)
        return good_list[0]

    def query_address(self,id):
        sql = 'select * from wklc_address where order_id=%s'
        detail = self.query(sql,id)
        if detail:
            return detail[0]

    def query_default(self,id):
        sql = 'select * from wklc_default_address where user_id=%s'
        detail = self.query(sql,id)
        if detail:
            return detail[0]

    def select_add(self,id):
        sql = 'select * from wklc_default_address where user_id=%s'
        resutle = self.query(sql,id)
        return not bool(resutle)

    def del_add(self,id):
        sql = 'delete from wklc_default_address where user_id=%s'
        resulte = self.delete(sql,id)
        return resulte

if __name__ == '__main__':
    dao = OrderDao()

    print(dao.query_address(44))