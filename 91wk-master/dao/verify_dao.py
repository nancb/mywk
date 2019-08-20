from dao import BaseDao


class Verify_Dao(BaseDao):
    #查询是否实名验证
    def user_verify(self,user_id):
        sql = 'select * from wklc_user_verify where user_id=%s'
        verify = self.query(sql,user_id)
        if verify:
            return verify[0]
        else:
            return False
    #实名认证
    def toverify(self,userName,userCard):
        sql = 'select * from wklc_verify where userName=%s and userCard=%s'
        verify = self.query(sql,userName,userCard)
        if verify:
            return verify[0]
        else:
            return False
    def save_verify(self, **values):
        return super(Verify_Dao, self).save('wklc_user_verify', **values)

    def update_user(self,user_id):
        sql = 'update wklc_users set is_Verify=1 where id=%s'
        result = self.update(sql,user_id)
        return result
    def query_user_verify(self,verify_id):
        sql = 'select * from wklc_user_verify ' \
              'where verify_id=%s'
        user_data = self.query(sql,verify_id)  # 返回用户对象
        if user_data:
            return user_data[0]
        else:
            return False


