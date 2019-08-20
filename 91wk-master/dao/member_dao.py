
from dao import BaseDao

class MembersDao(BaseDao):
    def show_members(self):
        sql = 'select * from wklc_members'
        all_members = self.query(sql)
        if all_members:
            return all_members