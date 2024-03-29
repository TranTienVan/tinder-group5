from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.forms import MyUserCreationForm, MyUserChangeForm
from authentication.models import MyUser
from tinder_profile.models import Members, MembersInfo, MembersSettings, MembersImages
from tinder.models import Reports

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class MembersAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_name')

class MembersInfoAdmin(admin.ModelAdmin):
    list_display = ('user', )

class MembersSettingsAdmin(admin.ModelAdmin):
    pass

class MembersImagesAdmin(admin.ModelAdmin):
    list_display = ('image_id', 'user')

class ReportsAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'type', 'created_date', 'status')


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(MembersInfo, MembersInfoAdmin)
admin.site.register(MembersSettings, MembersSettingsAdmin)
admin.site.register(MembersImages, MembersImagesAdmin)
admin.site.register(Reports, ReportsAdmin)
admin.site.site_header = 'Wanna Date Admin Portal'
admin.site.site_title = "Wanna Date Admin Portal"