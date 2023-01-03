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
    ORDID = models.AutoField(primary_key=True, null=False)
    PROID = models.CharField(max_length=20, null=True)
    PRONAME = models.CharField(max_length=20, null=True)
    MEMO = models.CharField(max_length=20, null=True)
    MEMID = models.CharField(max_length=20, null=False)
    CDATE = models.DateTimeField()
    GPOINT = models.IntegerField()
    BALANCE = models.IntegerField() # 此欄位要記得從member的GPOINT做更新
    AMOUNT = models.IntegerField(null=True)
    TIME = models.IntegerField()
    APPID = models.IntegerField() # 智慧喜組別
    def __str__(self):
        return self.MEMID

class product(models.Model):
    productID = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=20, null=False)
    productimage1 = models.CharField(max_length=50, null=False)
    productpoint = models.IntegerField()
    productlimit = models.IntegerField()
    def __str__(self):
        return self.productname

class rankinfo(models.Model):
    rankname = models.CharField(max_length=20, null=False)
    rankimg = models.CharField(max_length=20, null=False)
    def __str__(self):
        return self.rankname
