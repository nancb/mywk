import xadmin as admin

from products.models import ProductStyle, Product


class ProductStyleAdmin():
    list_display = ['productBigId','productBigName']
    search_fields = list_display
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-gbp'

admin.site.register(ProductStyle,ProductStyleAdmin)


class ProductAdmin():
    list_display = ['productId','productName','productRate',
                    'productCloseTime','minLend','placementCycle',
                    'produtBalance','productBig']
    search_fields = ['productId','productName','productRate',
                    'productCloseTime','minLend','placementCycle',
                    'produtBalance']
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-gbp'
    #list_editable = list_display

admin.site.register(Product,ProductAdmin)