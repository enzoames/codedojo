from django.contrib import admin
from dojoteam.models import DojoMember, DojoMemberType

# Register your models here.
# This lets the django administration that you want your database tables to be added

@admin .register(DojoMember, DojoMemberType)

class DefaultAdmin(admin.ModelAdmin):
    pass
