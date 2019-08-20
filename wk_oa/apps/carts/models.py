from django.db import models

from goods.models import Goods
from user.models import User

# 11.购物车模型
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='用户')    # 外键关联用户
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE,verbose_name='商品')  # 外键关联商品
    cart_goods_num = models.IntegerField(default=1,verbose_name='商品数量')         # 存储于购物车中的商品数量
    checked = models.BooleanField(default=True,verbose_name='是否被选中')            # 选中状态，默认选中

    def __int__(self):
        return self.goods

    class Meta:
        db_table = 'wklc_carts'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
