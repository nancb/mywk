import xadmin as  admin

from carts.models import Cart


class CartAdmin():
    list_display = ['cart_goods_num','goods','user','checked']
    search_fields = ['cart_goods_num','checked']
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-shopping-cart'
admin.site.register(Cart,CartAdmin)
