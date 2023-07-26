from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('receipts/', views.receipts_index, name='index'),
  path('receipts/<int:receipt_id>/', views.receipts_detail, name='detail')
]