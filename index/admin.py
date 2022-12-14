from django.contrib import admin

from index.models import *

# Register your models here.


admin.site.site_title = "学生公寓报修系统的设计与实现"
admin.site.site_header = "学生公寓报修系统的设计与实现"
admin.site.index_title = "学生公寓报修系统的设计与实现"


class UserManager(admin.ModelAdmin):
    # 列表页显示那些字段
    search_fields = ('name', 'phone')
    list_display = ['id', 'name', 'admin_sample', 'gender', 'phone', 'email', 'type', 'time']


class NoticeManager(admin.ModelAdmin):
    # 列表页显示那些字段
    search_fields = ('title', 'content')
    list_display = ['id', 'title', 'content', 'time', 'type']


class RepairManager(admin.ModelAdmin):
    list_display_links = ('id', 'single')
    search_fields = ('id', 'user', 'single')
    list_display = ['id', 'single', 'user', 'flor', 'type', 'title', 'time', 'admin_sample']


admin.site.register(User, UserManager)
admin.site.register(Notice, NoticeManager)
admin.site.register(Repair, RepairManager)
