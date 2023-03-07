from django.db import models
from assos_app.models import Mahsulot,Client,Ombor
# Create your models here.

class Statistika(models.Model):
  mahsulot=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
  client=models.ForeignKey(Client,on_delete=models.CASCADE)
  ombor=models.ForeignKey(Ombor,on_delete=models.CASCADE)
  miqdor=models.PositiveIntegerField()
  sana=models.DateTimeField(auto_now_add=True)
  umumi_suma=models.PositiveIntegerField()
  tolov=models.PositiveIntegerField()
  nasya=models.PositiveIntegerField()
  def __int__(self) -> str:
    return self.sana