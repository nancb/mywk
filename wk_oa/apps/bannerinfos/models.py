from django.db import models

# 7.轮播图模型
class BannerInfo(models.Model):
    url = models.CharField(max_length=255,verbose_name='轮播图地址')                  # 轮播图地址
    name = models.CharField(max_length=50,verbose_name='轮播图名称')                  # 轮播图名称

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wklc_bannerInfo'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
