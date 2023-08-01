from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Receipt, People
from datetime import date
from .forms import ExpenseForm


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
  expense_form = ExpenseForm
  return render(request, 'receipts/detail.html', {
    'receipt': receipt, 'expense_form': expense_form
  })

class ReceiptCreate(CreateView):
  model = Receipt
  fields = '__all__'

class ReceiptUpdate(UpdateView):
  model = Receipt
  fields = ['restaurant', 'date', 'total']

class ReceiptDelete(DeleteView):
  model = Receipt
  success_url = '/receipts'

def add_expense(request, receipt_id):
  form = ExpenseForm(request.POST)
  if form.is_valid():
    new_expense = form.save(commit=False)
    new_expense.receipt_id = receipt_id
    new_expense.save()
    return redirect('detail', receipt_id=receipt_id)
  
class PeopleList(ListView):
  model = People

class PersonDetail(DetailView):
  model = People

class PersonCreate(CreateView):
  model = People
  fields = '__all__'

class PersonUpdate(UpdateView):
  model = People
  fields = ['name']

class PersonDelete(DeleteView):
  model = People
  success_url = '/people'

def assoc_people(request, receipt_id, people_id):
  Receipt.objects.get(id=receipt_id).people.add(people_id)
  return redirect('detail', receipt_id=receipt_id)

def unassoc_people(request, receipt_id, people_id):
  Receipt.objects.get(id=receipt_id).people.remove(receipt_id)
  return redirect('detail', receipt_id=receipt_id)