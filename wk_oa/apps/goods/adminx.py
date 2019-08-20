import xadmin as admin
from goods.models import *

class GoodsInfoAdmin():
    list_display =['bigid','bigname','bigimgurl']
    search_fields = list_display
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-inbox'
admin.site.register(GoodsInfo,GoodsInfoAdmin)

class GoodsAdmin():
    list_display = ['goodsId','goodsName','kfCoin','big']
    search_fields = ['goodsId','goodsName','kfCoin']
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-inbox'
admin.site.register(Goods,GoodsAdmin)