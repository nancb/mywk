from dao import BaseDao


class CartDao(BaseDao):
    def save(self, **values):
        # api_logger.info('db insert wklc_users: <%s>' % values['userTel'])
        print(values)
        return super(CartDao, self).save('wklc_carts', **values)

    def check_cart(self,u_id,g_id):
        sql = 'select * from wklc_carts where user_id=%s and goods_id=%s'
        goods = self.query(sql,u_id,g_id)
        print("*************",goods)
        return goods[0]

    def check_login_name(self,u_id,g_id):
        result = self.query('select id from wklc_carts where user_id=%s and goods_id=%s',u_id,g_id)
        print(result)
        print(not bool(result))
        return not bool(result)

    def update_goods_num(self,u_id,g_id,g_num):
        sql = 'update wklc_carts set cart_goods_num=%s where user_id=%s and goods_id=%s'
        print(u_id,g_id,g_num)
        result = self.update(sql,g_num,u_id,g_id)
        return result

    def del_goods(self,u_id,g_id):
        sql = 'delete from wklc_carts where user_id=%s and goods_id=%s'
        result = self.delete(sql,u_id,g_id)
        return result

    def show_cars(self,u_id):
        sql = 'select * from wklc_carts where user_id=%s'
        cars = self.query(sql,u_id)
        return cars

    def show_sort(self,id):
        sql = 'select * from wklc_goods where goodsId=%s'
        good_list = self.query(sql,id)
        return good_list[0]

    def update_goods_checked(self,user_id,goods_id,checked):
        sql = 'update wklc_carts set checked=%s where user_id=%s and goods_id=%s'
        checkeds = self.update(sql,checked,user_id,goods_id)
        return checkeds



if __name__ == '__main__':
    dao1 = CartDao()
    # c = ["1","1"]
    # print(c)
    print(dao1.check_login_name("1","1"))