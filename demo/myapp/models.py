from django.db import models

# Create your models here.
class member(models.Model):
    account = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=10, null=False)
    email = models.EmailField(max_length=50, null=False)
    name = models.CharField(max_length=10, null=False)
    def __str__(self):
        return self.account