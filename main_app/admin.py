from django.contrib import admin
from .models import Receipt, Expense, People

# Register your models here.
admin.site.register(Receipt)
admin.site.register(Expense)
admin.site.register(People)