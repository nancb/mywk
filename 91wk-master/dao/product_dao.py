from flask import jsonify

from dao import BaseDao
from logger import api_logger


class ProductDao(BaseDao):
    def all_productstyles(self):
        sql = "select * from wklc_productstyles "
        all_productstyles = self.query(sql)
        if all_productstyles:
            return all_productstyles
    def all_products(self,productBigId):
        sql = "select * from wklc_products where productBig_id=%s"
        all_products = self.query(sql,productBigId)
        if all_products:
            return all_products
    def all_lendrecords(self,product_id):
        sql = "select * from wklc_lendrecords where product_id=%s"
        all_lendrecords = self.query(sql,product_id)
        if all_lendrecords:

            return all_lendrecords
    def all_lendInfo(self):
        sql = "select * from wklc_lendinfo"
        all_lendInfo = self.query(sql)
        if all_lendInfo:
            return all_lendInfo


