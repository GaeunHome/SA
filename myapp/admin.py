from django.contrib import admin
from myapp.models import member

class userAdmin(admin.ModelAdmin):
    list_display=('account','password','phone','email','name',)
# Register your models here.
admin.site.register(member, userAdmin)