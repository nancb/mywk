import xadmin as admin

from bannerinfos.models import BannerInfo


class BannerInfoAdmin():
    list_display = ['url','name']
    search_fields = list_display
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-asterisk'
admin.site.register(BannerInfo,BannerInfoAdmin)
