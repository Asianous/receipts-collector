from django.db import models
from django.urls import reverse

PAID = (
  ('P', 'Paid'),
  ('N', 'Not Paid Yet')
)

class People(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
  
  def get_absolute_url(self):
    return reverse('people_detail', kwargs={'pk': self.id})

# Create your models here.
class Receipt(models.Model):
  name = models.CharField(max_length=100, null=True)
  restaurant = models.CharField(max_length=100)
  datepick = models.DateField(auto_now=False)
  total = models.DecimalField(max_digits=6, decimal_places=2)
  people = models.ManyToManyField(People)

  def __str__(self):
    return f'{self.name} ({self.id})'
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'receipt_id': self.id})

class Expense(models.Model):
  paid = models.CharField(
    max_length=1,
    choices=PAID,
    default=[1][0]
  )
  date = models.DateField('Date')

  receipt = models.ForeignKey(
    Receipt, on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_paid_display()} on {self.date}"