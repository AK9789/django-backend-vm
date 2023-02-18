from django.db import models
from accounts.models import User

# Create your models here.
class Tpp(models.Model):
    u_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    T_id = models.AutoField(primary_key=True)
    T_name = models.CharField(max_length=100)
    T_bankName = models.CharField(max_length=100)
    T_accountNo = models.IntegerField(default=0)
    T_ifsc = models.CharField(max_length=100)
    T_branch = models.CharField(max_length=100)
