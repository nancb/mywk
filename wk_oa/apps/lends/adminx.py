import xadmin as admin
from lends.models import LendRecord, LendInfo


class LendRecordAdmin():
    list_display = ['lendUserTel','lendMoney','lendTime',
                    'product','user']
    search_fields = ['lendUserTel','lendMoney','lendTime']
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-log-out'

admin.site.register(LendRecord,LendRecordAdmin)

class LendInfoAdmin():
    list_display = ['lendPurpose','beginDate','personCode',
                    'returnStyle','incomeSources','industry']
    search_fields = list_display
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-log-out'

admin.site.register(LendInfo,LendInfoAdmin)