from django.db import models
from orders.models import Orders
from user.models import User

# 18.用户添加的收货地址

class Default_Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')  # 用户
    userName = models.CharField(max_length=30,verbose_name='用户姓名') # 用户姓名
    userPhone = models.CharField(max_length=50,verbose_name='用户电话') # 用户电话
    address = models.CharField(max_length=255,verbose_name= '地址') # 地址
    detailAddress = models.CharField(max_length=255,verbose_name='详细地址') # 详细地址
    postalCode = models.CharField(max_length=20,verbose_name='邮政编码') # 邮政编码

    def __str__(self):
        return self.userName

    class Meta:
        db_table = 'wklc_default_address'
        verbose_name = '用户默认收货地址'
        verbose_name_plural = verbose_name

# 19. 用户收货地址
class Address(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='订单')  # 关联订单
    userName = models.CharField(max_length=30, verbose_name='用户姓名')  # 用户姓名
    userPhone = models.CharField(max_length=50, verbose_name='用户电话')  # 用户电话
    address = models.CharField(max_length=255, verbose_name='地址')  # 地址
    detailAddress = models.CharField(max_length=255, verbose_name='详细地址')  # 详细地址
    postalCode = models.CharField(max_length=20, verbose_name='邮政编码')  # 邮政编码

    def __str__(self):
        return self.userName

    class Meta:
        db_table = 'wklc_address'
        verbose_name = '用户收货地址'
        verbose_name_plural = verbose_name