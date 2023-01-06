from django.contrib import admin
from myapp.models import member, question, transaction, product, rankinfo

class userAdmin(admin.ModelAdmin):
    list_display=('account','password','phone','email','name','GPOINT')
# Register your models here.
admin.site.register(member, userAdmin)

class questionAdmin(admin.ModelAdmin):
    list_display=('account','question')
admin.site.register(question, questionAdmin)

class transactionAdmin(admin.ModelAdmin):
    list_display=('ORDID','PROID','MEMO','MEMID','CDATE','GPOINT','AMOUNT','APPID')
admin.site.register(transaction, transactionAdmin)

class productAdmin(admin.ModelAdmin):
    list_display=('productID','productname','productimage1','productpoint','productlimit','productkind')
admin.site.register(product, productAdmin)

class rankAdmin(admin.ModelAdmin):
    list_display=('rankname','rankengname','rankimg','rankpoint')
admin.site.register(rankinfo, rankAdmin)

