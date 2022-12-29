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