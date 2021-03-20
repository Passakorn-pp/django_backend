from django.contrib import admin
from loginline.models import UserLine,Dormitory,Room,filterDo,filterDormitory,DataUser,Question,Answer,History,HistoryNouser,Like,Imgall

class FilterDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', "wifi")

admin.site.register(UserLine)
admin.site.register(Dormitory)
admin.site.register(Room)
admin.site.register(filterDo, FilterDoAdmin)
admin.site.register(filterDormitory)
admin.site.register(DataUser)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(History)
admin.site.register(HistoryNouser)
admin.site.register(Like)
admin.site.register(Imgall)
