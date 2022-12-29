from django.db import models

# Create your models here.
class member(models.Model):
    account = models.CharField(primary_key=True, max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=10, null=False)
    email = models.EmailField(max_length=50, null=False)
    name = models.CharField(max_length=10, null=False)
    GPOINT = models.IntegerField()
    def __str__(self):
        return self.account

class question(models.Model):
    account = models.CharField(max_length=20)
    question = models.CharField(max_length=500)
    def __str__(self):
        return self.account

class transaction(models.Model):
    ORDID = models.CharField(primary_key=True, max_length=20, null=False)
    MEMO = models.CharField(max_length=20)
    MEMID = models.CharField(max_length=20, null=False)
    CDATE = models.DateTimeField()
    GPOINT = models.IntegerField()
    BALANCE = models.IntegerField() # 此欄位要記得從member的GPOINT做更新
    AMOUNT = models.IntegerField()
    APPID = models.IntegerField() # 智慧喜組別
    def __str__(self):
        return self.MEMID
