from django.db import models
from django.contrib import admin
# Create your models here.

class People(models.Model): 
    name = models.CharField(max_length=100)
    designation = models.IntegerField()
    photo = models.ImageField(upload_to='photos/')

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name','designation','photo')

class Product(models.Model): 
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price' ,'photo')

