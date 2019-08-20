from django.db import models
from members.models import Members
from user.helper import make_password

# 1.用户模型
class User(models.Model):

    userName = models.CharField(max_length=20,verbose_name='用户姓名')              # 用户姓名
    userTel = models.CharField(max_length=20,unique=True,verbose_name='用户电话')   # 用户电话,设置唯一
    userPic = models.CharField(max_length=500,default=None,verbose_name='用户头像')    # 用户电话
    password = models.CharField(max_length=256,verbose_name='用户密码')              # 用户密码
    userGrade = models.ForeignKey(Members, on_delete=models.CASCADE, verbose_name='会员等级')  # 用户会员等级
    totalMoney = models.FloatField(default=5000.00,verbose_name='总资产')           # 用户总资产
    yersterdayReturn = models.FloatField(verbose_name='昨日期望回报')               # 昨日期望回报
    totalReturn = models.FloatField(verbose_name='累计期望回报')                    # 累计期望回报
    userKfCoin = models.IntegerField(default=500000,verbose_name='空粉币')          # 我的空粉币 默认100
    userfuZuan = models.FloatField(default=0.0,verbose_name='富钻')                 # 我的富钻 默认为0.0
    zyMoney = models.FloatField(verbose_name= '自有本金')                           # 自由本金
    xyMoney = models.FloatField(verbose_name= '虚有本金')                           # 须有本金
    is_Verify = models.BooleanField(default=False, verbose_name='是否验证')         # 是否验证

    def __str__(self):
        return self.userName

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.password) < 32:
            self.password = make_password(self.password)
        super().save()

    class Meta:
        db_table = 'wklc_users'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

# 2.用户回报金额模型
class Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')     # 用户
    monthAccount = models.FloatField(default=0.0,verbose_name='月账户回报金额')     # 月账户回报金额
    sensonAccount = models.FloatField(default=0.0,verbose_name='季账户回报金额')    # 季账户回报金额
    yearAccount = models.FloatField(default=0.0,verbose_name='年账户回报金额')      # 年账户回报金额
    specialAccount = models.FloatField(default=0.0,verbose_name='特殊账户期望回报') # 特殊账户期望回报
    virtualPrincipal = models.FloatField(default=0.0,verbose_name= '虚拟本金')      # 虚拟本金

    def __int__(self):
        return self.user

    class Meta:
        db_table = 'wklc_accounts'
        verbose_name = '用户回报金额'
        verbose_name_plural = verbose_name

# 14.身份验证模型
class Verify(models.Model):
    userName = models.CharField(max_length=20,verbose_name='用户姓名')              # 用户姓名
    userCard = models.CharField(max_length=30,verbose_name='用户身份证')            # 用户身份证

    def __str__(self):
        return self.userName

    class Meta:
        db_table = 'wklc_verify'
        verbose_name = '用户身份验证'
        verbose_name_plural = verbose_name

# 15.用户验证关联模型
class User_Verify(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')   # 用户
    verify = models.ForeignKey(Verify,on_delete=models.CASCADE,verbose_name='验证') # 验证

    def __int__(self):
        return self.user

    class Meta:
        db_table = 'wklc_user_verify'
        verbose_name = '用户验证关联'
        verbose_name_plural = verbose_name

# 16.银行卡模型
class Card(models.Model):
    cardNum = models.CharField(max_length=255,verbose_name='卡号')            # 卡号
    cardTel = models.CharField(max_length=255,verbose_name='卡预留手机号')    # 卡预留手机号
    cardPwd = models.CharField(max_length=255,verbose_name='App支付密码')     # App支付密码
    cardMoney = models.FloatField(verbose_name='卡账户余额')                  # 卡账户余额

    def __str__(self):
        return self.cardNum

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.cardPwd) < 32:
            self.cardPwd = make_password(self.cardPwd)
        super().save()

    class Meta:
        db_table = 'wklc_cards'
        verbose_name = '用户银行卡绑定'
        verbose_name_plural = verbose_name

# 17.用户卡关联模型
class User_Card(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')       #用户
    card = models.ForeignKey(Card,on_delete=models.CASCADE,verbose_name= '银行卡')     # 银行卡

    def __int__(self):
        return self.user

    class Meta:
        db_table = 'wklc_user_card'
        verbose_name = '用户银行卡关联'
        verbose_name_plural = verbose_name
