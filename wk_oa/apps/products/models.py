from django.db import models

# 3.理财产品大类模型
class ProductStyle(models.Model):
    productBigId = models.IntegerField(primary_key=True,verbose_name = '理财产品大类ID')           # 理财产品大类ID
    productBigName = models.CharField(max_length=255,verbose_name='大类名称')     # 大类名称

    def __str__(self):
        return self.productBigName

    class Meta:
        db_table = 'wklc_productstyles'
        verbose_name = '理财产品类型'
        verbose_name_plural = verbose_name

# 4.理财产品模型
class Product(models.Model):
    productBig =models.ForeignKey(ProductStyle,on_delete=models.CASCADE,verbose_name='理财产品大类') # 理财产品大类ID
    productId = models.IntegerField(primary_key=True,verbose_name= '理财产品ID')   # 理财产品ID
    productName = models.CharField(max_length=50,verbose_name='理财产品名称')      # 理财产品名称
    productRate = models.FloatField(verbose_name='期望回报率')                     # 期望回报率
    productCloseTime = models.IntegerField(verbose_name='封闭期限')                # 封闭期限
    minLend = models.IntegerField(default=100,verbose_name='最低出借')             # 最低出借
    placementCycle = models.DateTimeField(verbose_name='剩余时间')                 # 剩余时间
    produtBalance = models.FloatField(default=1000000,verbose_name='剩余金额')     # 剩余金额

    def __str__(self):
        return self.productName

    class Meta:
        db_table = 'wklc_products'
        verbose_name = '理财产品信息'
        verbose_name_plural = verbose_name
