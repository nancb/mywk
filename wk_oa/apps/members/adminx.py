import xadmin as admin

from members.models import Members


class MembersAdmin():
    list_display = ['userGrade','equity','canLend']
    search_fields = list_display
    list_filter = list_display
    list_per_page = 20
    model_icon = 'glyphicon glyphicon-cloud'
admin.site.register(Members,MembersAdmin)
