from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.views import View


# Create your views here.

# <----Bolimview------------>
class BulimView(View):
  def get(self,request):
    if request.user.is_authenticated :
      return render(request,'bulimlar.html')
    return redirect('login')


#<-------- login View---------->
class LoginView(View):
  def get(self,request):
    return render(request,'home.html')
  
  def post(self,request):
    n=authenticate(username=request.POST.get('login'),
                   password=request.POST.get('password'))
    if n is None:
      login(request,n)
      return redirect('login')
    return redirect('bulim')
  
#-------------logoutView------------------->
class LogoutView(View):
  def get(self,request):
    logout(request)
    return redirect('login')
  
  
# <--------------- Product--------------->
class ProductsView(View):
  def get(self,request):
    if request.user.is_authenticated:
      ombor_1=Ombor.objects.get(user=request.user)
      soz=request.GET.get('qidirish')
      if soz is None:
        P_R=Mahsulot.objects.filter(ombor=ombor_1)
      else:
        P_R=Mahsulot.objects.filter(ombor=ombor_1,nom__contains=soz)
      data={
        'mahsulotlar':P_R
      }
      return render(request,'products.html',data)
    redirect('bulim')
  
  def post(self,request):
    Mahsulot.objects.create(
      nom=request.POST.get('pr_name'),
      brend=request.POST.get('pr_brend'),
      narx=request.POST.get('pr_price'),
      miqdor=request.POST.get('pr_amount'),
      olchov=request.POST.get('pr_olchov'),
      kelgan_sana=request.POST.get('pr_date'),
      ombor=Ombor.objects.get(user=request.user)
    )
    return redirect('mahsulot')
  
  
#<----------------Product_Delet---------------->
class ProductDeletView(View):
  def get(self,request,pk):
    mahsulot=Mahsulot.objects.get(id=pk)
    if Ombor.objects.get(user=request.user) == mahsulot.ombor:
      mahsulot.delete()
    return redirect('mahsulot')
  
  
# <------------------Proguct_update--------------------->
class ProductUpdate(View):
  def get(self,request,pk):
    mahsulot_1=Mahsulot.objects.get(id=pk)
    if Ombor.objects.get(user=request.user) == mahsulot_1.ombor:
      data={
        'product':mahsulot_1
      }
      return render(request,'product_update.html',data)
    return redirect('mahsulot')
  
  
  def post(self,request,pk):
    m1=Mahsulot.objects.filter(id=pk)
    m1.update(
      narx=request.POST.get('price'),
      miqdor=request.POST.get('amount'),
    )
    return redirect('mahsulot')



#<------------------Client---------------->
class ClientView(View):
  def get(self,request):
    if request.user.is_authenticated:
      client1=Ombor.objects.get(user=request.user)
      soz=request.GET.get('qidirish')
      if soz is None:
        c_q=Client.objects.filter(ombor=client1)
      else:
        c_q=Client.objects.filter(ombor=client1,nom__contains=soz)
      data={
       "clinetlar":c_q
      }
      return render(request,'clients.html',data)
    return redirect('bulim')
  
  def post(self,request):
    Client.objects.create(
      ism=request.POST.get('client_name'),
      nom=request.POST.get('client_shop'),
      tel=request.POST.get('client_phone'),
      manzil=request.POST.get('client_address'),
      qarz=request.POST.get('client_DEBT'),
      ombor=Ombor.objects.get(user=request.user)
    )
    return redirect('client')
  
  
  
#<----------------Clienr_Delet---------------->
class ClientDeletView(View):
  def get(self,request,pk):
    client=Client.objects.get(id=pk)
    if Ombor.objects.get(user=request.user) == client.ombor:
      client.delete()
    return redirect('client')
  

#<----------------Client_Update------------------------>
class ClientUpdateView(View):
  def get(self,request,pk):
    client_1=Client.objects.get(id=pk)
    if Ombor.objects.get(user=request.user) == client_1.ombor:
      data={
        'client':client_1
      }
      return render(request,'client_update.html',data)
    return redirect('client')
  
  def post(self,request,pk):
    c_1=Client.objects.get(id=pk)
    c_1.update(
      ism=request.POST.get('client_name'),
      tel=request.POST.get('client_phone'),
      qarz=request.POST.get('client_debt'),
    )
    return redirect('client')
      


