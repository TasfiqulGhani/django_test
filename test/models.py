from django.db import models


# Create your models here.


class CustomerInfo(models.Model):
    CustomerId = models.CharField(max_length=10, default='', unique=True)
    CustomerName = models.CharField(max_length=200, default='', unique=False)
