
import xadmin as admin

from user.models import *
from user.forms import UserForm, CardForm


class UserAdmin():
    form = UserForm
    list_display = ['userName','userTel','totalMoney','userGrade',
                    'yersterdayReturn','totalReturn','userKfCoin',
                    'userfuZuan','zyMoney','xyMoney','is_Verify','userPic']
    search_fields = ['userName','userTel']
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-user'
    refresh_times = (60, 120)
admin.site.register(User,UserAdmin)

class AccountAdmin():

    list_display =['monthAccount','sensonAccount','yearAccount',
                   'specialAccount','virtualPrincipal','user']
    search_fields = ['monthAccount','sensonAccount','yearAccount',
                   'specialAccount','virtualPrincipal']
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-user'

admin.site.register(Account,AccountAdmin)

class VerifyAdmin():

    list_display =['userName','userCard']
    search_fields = list_display
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-user'
admin.site.register(Verify,VerifyAdmin)

class User_VerifyAdmin():

    list_display = ['user','verify']
    model_icon = 'glyphicon glyphicon-user'
admin.site.register(User_Verify,User_VerifyAdmin)

class CardAdmin():
    form = CardForm
    list_display = ['cardNum','cardTel','cardPwd','cardMoney']
    search_fields = list_display
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-user'
admin.site.register(Card,CardAdmin)

class User_CardAdmin():

    list_display = ['user','card']
    model_icon = 'glyphicon glyphicon-user'
admin.site.register(User_Card,User_CardAdmin)