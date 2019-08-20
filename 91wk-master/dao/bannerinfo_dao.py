
from dao import BaseDao

class BannerInfoDao(BaseDao):
    def show_bannerinfo(self):
        sql = 'select * from wklc_bannerInfo'
        all_bannerinfo = self.query(sql)
        if all_bannerinfo:
            return all_bannerinfo