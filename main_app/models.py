from django.db import models


# Create your models here.
class Receipt(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField()
  total = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return f'{self.title} ({self.id})'
