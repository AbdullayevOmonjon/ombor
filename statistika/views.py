from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.contrib.auth import authenticate
# Create your views here.


class StatitikaView(View):
  def get(self,request):
    if request.user.is_authenticated:
      s=Ombor.objects.get(user=request.user)
      data={
        'statistikalar':Statistika.objects.filter(ombor=s)
      }
      return render(request,'stats.html')
    return redirect('bulim')