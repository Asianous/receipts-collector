from django.db import models
from django.urls import reverse


# Create your models here.
class Receipt(models.Model):
  name = models.CharField(max_length=100, null=True)
  restaurant = models.CharField(max_length=100)
  date = models.DateField(auto_now=False)
  total = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return f'{self.name} ({self.id})'
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'receipt_id': self.id})
