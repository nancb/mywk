import xadmin as admin

from address.models import *

class Default_AddressAdmin():
    list_display = ['userName','userPhone','address',
                    'detailAddress','postalCode']
    search_fields = list_display
    list_filter = list_display
    list_per_page = 2 
    model_icon = 'glyphicon glyphicon-envelope'
admin.site.register(Default_Address,Default_AddressAdmin)

class AddressAdmin():
    list_display = ['userName', 'userPhone', 'address',
                    'detailAddress', 'postalCode']
    search_fields = list_display
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-envelope'

admin.site.register(Address, AddressAdmin)

