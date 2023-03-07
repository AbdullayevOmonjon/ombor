from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.contrib.auth import authenticate
# Create your views here.


class StatitikaView(View):
  def get(self,request):
    if request.user.is_authenticated:
      s=Ombor.objects.get(user=request.user)
      soz=request.GET.get('qidirish')
      if soz is None:
        s_t=Statistika.objects.filter(ombor=s)
      else:
        s_t=Statistika.objects.filter(ombor=s,mahsulot__contains=soz,client__contains=soz,ombor__contains=soz)
      data={
        'statistikalar':s_t
      }
      return render(request,'stats.html')
    return redirect('bulim')