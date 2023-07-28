from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('receipts/', views.receipts_index, name='index'),
  path('receipts/<int:receipt_id>/', views.receipts_detail, name='detail'),
  path('receipts/create/', views.ReceiptCreate.as_view(), name='receipt_create'),
  path('receipts/<int:pk>/update/', views.ReceiptUpdate.as_view(), name='receipt_update'),
  path('receipts/<int:pk>/delete/', views.ReceiptDelete.as_view(), name='receipt_delete'),
]