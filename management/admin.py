from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from management.models import *
# Register your models here.


class MyUserInline(admin.StackedInline):
    model = MyUser
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (MyUserInline,)

class MyAdminSite(admin.AdminSite):
    admin.site.site_header = '医疗信息管理系统'
    admin.site.site_title = '王晓康医疗管理'

admin_site = MyAdminSite(name='management')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(BOOK)
admin.site.register(Img)
