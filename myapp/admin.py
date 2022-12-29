from django.contrib import admin
from myapp.models import member, question, transaction

class userAdmin(admin.ModelAdmin):
    list_display=('account','password','phone','email','name','GPOINT')
# Register your models here.
admin.site.register(member, userAdmin)

class questionAdmin(admin.ModelAdmin):
    list_display=('account','question')
admin.site.register(question, questionAdmin)

class transactionAdmin(admin.ModelAdmin):
    list_display=('ORDID','MEMID','CDATE','GPOINT','AMOUNT','APPID')
admin.site.register(transaction, transactionAdmin)