from django.db import models

# 9.商品大类模型

class GoodsInfo(models.Model):
    bigid = models.IntegerField(primary_key=True,verbose_name='商品大类ID')                             # 商品大类id
    bigname = models.CharField(max_length=50,verbose_name='商品大类名称')              # 商品大类名称
    bigimgurl = models.CharField(max_length=255,default=None,verbose_name='图片地址')            # 图片地址

    def __str__(self):
        return self.bigname

    class Meta:
        db_table = 'wklc_goodsinfo'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name

# 10.商品模型
class Goods(models.Model):
    big = models.ForeignKey(GoodsInfo,on_delete=models.CASCADE,verbose_name='商品大类') # 商品大类
    goodsId = models.IntegerField(primary_key=True,verbose_name='商品ID')             # 商品id
    goodsName = models.CharField(max_length=255,verbose_name='商品名称')           # 商品名称
    isHot = models.BooleanField(default=False,verbose_name='是否热卖')              # 是否热卖 默认False
    isRecommend = models.BooleanField(default=False,verbose_name='是否推荐')        # 是否推荐 默认False
    littlePic = models.CharField(max_length=500,verbose_name='图片地址')            # 商品图片地址
    urplussNum = models.IntegerField(default=100,verbose_name='剩余商品数量')               # 剩余商品数量 默认为1
    isDiscountFirst = models.BooleanField(default=True,verbose_name='首次购买是否优惠')     # 首次购买是否五折优惠
    isNew = models.BooleanField(default=False,verbose_name='是否新品')              # 是否新品  默认False
    isBoutique = models.BooleanField(default=False,verbose_name='是否精品')         # 是否精品  默认False
    kfCoin = models.IntegerField(verbose_name='所需空粉币')                         # 商品所需空粉币
    fuZuan = models.FloatField(default=0.0,verbose_name='所需富钻')                 # 商品所需富钻 默认位0.0
    goodsDescribe = models.CharField(max_length=255,verbose_name='商品描述')        # 商品描述
    goodsSpecification = models.CharField(max_length=255,verbose_name='商品规格')   # 商品规格
    goodsDetails = models.CharField(max_length=500,verbose_name= '商品参数图片地址')# 商品参数图片地址

    def __str__(self):
        return self.goodsName

    class Meta:
        db_table = 'wklc_goods'
        verbose_name = '商品详情'
        verbose_name_plural = verbose_name
