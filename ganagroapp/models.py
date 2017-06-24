from django.db import models
from django.conf import settings
from django.utils import timezone
from PIL import Image as img
class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    ci = models.CharField(max_length=9)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.ci
        return self.phone
        return self.city


class Product(models.Model):
    client = models.ForeignKey('Client')
    category = models.ForeignKey('Category')
    product = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=100)
    location = models.CharField(max_length=100,default='trinidad')
    description = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
            return self.product
            return self.description
            return str(self.created_date)

class Image(models.Model):
    product = models.ForeignKey('Product')
    image = models.ImageField(upload_to='products')
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False )
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False)

    def __unicode__(self):
        return "{0}".format(self.image)

    def save(self):
        if not self.image:
            return

        super(Image, self).save()

        image = img.open(self.image)
        (width, height) = image.size
        size = ( 500, 300)
        image = image.resize(size)
        image.save(self.image.path)


class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Token(models.Model):
    token=models.TextField()
    def __str__(self):
        return self.token
# Create your models here.
