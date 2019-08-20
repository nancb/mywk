import xadmin as admin

from orders.models import *


class OrdersAdmin():
    list_display =['totalkfCoin','totalfuZuan','user',"orderNum",'pay']
    search_fields = ['totalkfCoin','totalfuZuan','orderNum']
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-calendar'
admin.site.register(Orders,OrdersAdmin)

class OrderDetailAdmin():
    list_display = ['order_goods_num','goods','order']
    search_fields = ['order_goods_num']
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-calendar'
admin.site.register(OrderDetail,OrderDetailAdmin)
