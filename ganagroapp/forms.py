from django import forms
from .models import Product, Image
from django.forms.extras.widgets import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['product'].widget.attrs = {'class' : 'form-control', 'required': 'required', 'placeholder': 'Titulo del anuncio'}
        self.fields['description'].widget.attrs = {'class' : 'form-control', 'required': 'required', 'placeholder': 'Descripcion del anuncio'}
        self.fields['category'].widget.attrs = {'class' : 'form-control', 'required': 'required'}
    class Meta:
        model = Product
        fields = ('product','description','category')

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = {"username","email","first_name","last_name"}
        def clean_email(self):
            email = self.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email already exists")
            return email
        def clean(self):
            form_data = self.cleaned_data
            if form_data['password'] != form_data['password']:
                self._errors["password"] = "password do not match"
                del form_data["password"]
            return form_data


    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control', 'required': 'required'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control', 'required': 'required'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control', 'required': 'required'})
        self.fields['password1'].widget.attrs.update({'class' : 'form-control', 'required': 'required'})
        self.fields['password2'].widget.attrs.update({'class' : 'form-control', 'required': 'required'})
