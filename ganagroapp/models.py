from django.db import models
from django.conf import settings

class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    ci = models.CharField(max_length=9)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.ci
        return self.birth_date
        return self.phone
        return self.city


class Product(models.Model):
    client = models.ForeignKey('Client')
    subcategory = models.OneToOneField('SubCategory')
    product = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.subcategory
        return self.product
        return self.description


class SubCategory(models.Model):
    category = models.OneToOneField('Category')
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
# Create your models here.
