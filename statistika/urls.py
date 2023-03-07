from django.urls import path
from .views import *


urlpatterns=[
  path('',StatitikaView.as_view(),name='statik')
]