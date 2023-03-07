from django.urls import path
from .views import *



urlpatterns=[
  path('bulim/',BulimView.as_view(),name='bulim'),
  path('mahsulot/',ProductsView.as_view(),name='mahsulot'),
  path('client/',ClientView.as_view(),name='client'),
  path('pr_delet/<int:pk>',ProductDeletView.as_view(),name='pr_delete'),
  path('pr_update/<int:pk>',ProductUpdate.as_view(),name='pr_update'),
  path('cl_delet/<int:pk>',ClientDeletView.as_view(),name='cl_delete'),
  path('cl_update/<int:pk>',ClientUpdateView.as_view(),name='cl_update'),
]