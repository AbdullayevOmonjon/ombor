from django.contrib.auth.models import User,AnonymousUser
from django.db import models


# ombor models
class Ombor(models.Model):
  nom=models.CharField(max_length=50)
  manzil=models.CharField(max_length=50)
  ism=models.CharField(max_length=25)
  tel=models.CharField(max_length=16)
  user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
  def __str__(self) -> str:
    return self.nom
  
  
# client models
class Client(models.Model):
  nom=models.CharField(max_length=50)
  manzil=models.CharField(max_length=50)
  ism=models.CharField(max_length=25)
  tel=models.CharField(max_length=16)
  qarz=models.PositiveIntegerField(default=0)
  ombor=models.ForeignKey(Ombor,on_delete=models.CASCADE,related_name='clintlar')
  def __str__(self) -> str:
    return self.nom
  
# mahsulot models
class Mahsulot(models.Model):
  nom=models.CharField(max_length=50)
  brend=models.CharField(max_length=50)
  miqdor=models.PositiveSmallIntegerField()
  narx=models.PositiveIntegerField()
  olchov=models.CharField(max_length=15)
  kelgan_sana=models.DateTimeField(auto_now_add=True)
  ombor=models.ForeignKey(Ombor,on_delete=models.CASCADE,related_name='mahsulotlar')
  def __str__(self) -> str:
    return self.nom