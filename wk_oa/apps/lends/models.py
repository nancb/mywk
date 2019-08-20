from django.db import models

from products.models import Product
from user.models import User

# 5.出借记录模型
class LendRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')  # 外键关联用户表
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='理财产品')   # 关联理财产品模型
    lendUserTel = models.CharField(max_length=50,verbose_name='出借人电话')            # 出借人手机号
    lendMoney = models.FloatField(verbose_name='出借金额')                          # 出借金额
    lendTime = models.DateTimeField(auto_now=True,verbose_name='出借时间')          # 出借时间，默认现在
    is_past = models.BooleanField(default=0,verbose_name='是否过期')                # 是否过期

    def __str__(self):
        return self.lendUserTel

    class Meta:
        db_table = 'wklc_lendrecords'
        verbose_name = '出借记录'
        verbose_name_plural = verbose_name

# 6. 借款信息披漏
class LendInfo(models.Model):
    lendPurpose = models.CharField(max_length=255,verbose_name='借款用途')          # 借款用途
    contractPrice = models.FloatField(verbose_name='合同金额')                     # 合同金额
    contractRate = models.FloatField(verbose_name='合同利率')                      # 合同利率
    contractLine = models.IntegerField(verbose_name='合同期限')                    # 合同期限
    personName = models.CharField(max_length=20,verbose_name='借款人姓名')          # 借款人姓名
    itemName = models.CharField(max_length=50,verbose_name='理财名称')              # 项目名称
    itemDetail = models.CharField(max_length=255,verbose_name='理财简介')           # 项目简介
    personCode = models.CharField(max_length=50,verbose_name='借款人身份证')        # 借款人身份证
    beginDate = models.CharField(max_length=20,verbose_name='起息日')               # 起息日
    returnStyle = models.CharField(max_length=30,verbose_name='还款方式')           # 还款方式
    limitOut = models.BooleanField(verbose_name='是否超限')                         # 是否超过限额
    returnProtect = models.CharField(max_length=255,verbose_name='还款保障措施')    # 还款保障措施
    returnFrom = models.CharField(max_length=255,verbose_name='还款来源')           # 还款来源
    incomeSources = models.CharField(max_length=255,verbose_name='收入')            # 收入
    industry = models.CharField(max_length=255,verbose_name='行业')                 # 行业
    hasLoan = models.BooleanField(verbose_name='是否有贷款')                        # 是否有贷款
    hasReport = models.BooleanField(verbose_name='征信报告')                        # 是否已提供征信报告
    otherLeand = models.BooleanField(verbose_name='其他平台贷款')                   # 是否有其他平台贷款
    otherLeandPrice = models.FloatField(verbose_name='其他平台贷款金额')            # 其他平台贷款金额
    productNameEve = models.CharField(max_length=255,verbose_name='产品金额')       # 产品金额
    beOverdueTimes = models.IntegerField(verbose_name='逾期次数')                   # 本平台逾期次数
    beOverduePrice = models.FloatField(verbose_name='逾期总金额')                   # 逾期总金额
    beOverrules = models.CharField(max_length=255,verbose_name='逾期利息')          # 逾期利息规则

    def __str__(self):
        return self.lendPurpose

    class Meta:
        db_table = 'wklc_lendinfo'
        verbose_name = '出借信息披漏'
        verbose_name_plural = verbose_name
