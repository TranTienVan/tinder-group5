from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Members)
admin.site.register(MembersInfo)
admin.site.register(MembersSettings)
admin.site.register(MembersImages)