from django.contrib import admin
from .models import Client,Product,Category,Image,Token
admin.site.register(Token)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Image)
# Register your models here.
