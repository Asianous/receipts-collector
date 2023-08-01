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
  path('receipts/<int:receipt_id>/add_expense/', views.add_expense, name='add_expense'),
  path('receipt/<int:receipt_id>/assoc_people/<int:people_id>/', views.assoc_people, name='assoc_people'),
  path('receipt/<int:receipt_id>/unassoc_people/<int:people_id>/', views.unassoc_people, name='unassoc_people'),
  path('people/', views.PeopleList.as_view(), name='people_index'),
  path('people/<int:pk>/', views.PersonDetail.as_view(), name='people_detail'),
  path('people/create/', views.PersonCreate.as_view(), name='people_create'),
  path('people/<int:pk>/update', views.PersonUpdate.as_view(), name='people_update'),
  path('people/<int:pk>/delete', views.PersonDelete.as_view(), name='people_delete'),

]