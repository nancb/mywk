from django.db import models
from user.models import User
from goods.models import Goods

# 12.订单模型
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='用户')    # 订单关联的用户
    totalkfCoin = models.IntegerField(verbose_name='共需空粉币')                    # 此次订单总共的空粉币
    totalfuZuan = models.FloatField(default=0.0,verbose_name='共需富钻')            # 此次订单总共的富钻
    pay = models.BooleanField(verbose_name='是否支付')                              # 是否支付
    orderNum = models.CharField(max_length=255,default=None,verbose_name= '订单号')              # 订单号

    def __str__(self):
        return self.orderNum

    class Meta:
        db_table = 'wklc_orders'
        verbose_name = '订单'
        verbose_name_plural = verbose_name

# 13.订单详情模型
class OrderDetail(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE,verbose_name='订单')  # 关联订单
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE,verbose_name='商品')   # 关联的商品
    order_goods_num = models.IntegerField(verbose_name='商品数量')                     # 在订单中该商品的数量

    def __int__(self):
        return self.order

    class Meta:
        db_table = "wklc_orderdetail"
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name
