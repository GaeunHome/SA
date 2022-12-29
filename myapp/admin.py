from django.contrib import admin
from myapp.models import member, question

class userAdmin(admin.ModelAdmin):
    list_display=('account','password','phone','email','name','GPOINT')
# Register your models here.
admin.site.register(member, userAdmin)

class questionAdmin(admin.ModelAdmin):
    list_display=('account','question')
admin.site.register(question, questionAdmin)