from django.shortcuts import render
from .models import Receipt


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def receipts_index(request):
  receipts = Receipt.objects.all()
  return render (request, 'receipts/index.html', {
    'receipts': receipts
  })

def receipts_detail(request, receipt_id):
  receipt = Receipt.objects.get(id=receipt_id)
  return render(request, 'receipts/detail.html', {
    'receipt': receipt
  })