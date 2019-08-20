from django.db import models

# 8.会员等级模型
class Members(models.Model):
    userGrade = models.CharField(max_length=255,verbose_name='用户会员等级') # 用户会员等级
    equity = models.CharField(max_length=255,verbose_name='解锁权益')                  # 解锁下一级会员的权益
    canLend = models.FloatField(verbose_name='可借出金额')                            # 可借出的金额

    def __str__(self):
        return self.userGrade

    class Meta:
        db_table = 'wklc_members'
        verbose_name = '会员等级'
        verbose_name_plural = verbose_name
