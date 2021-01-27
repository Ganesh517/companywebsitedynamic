from django.contrib import admin
from .models import People,PeopleAdmin
from .models import Product,ProductAdmin

# Register your models here.

admin.site.register(People,PeopleAdmin)

admin.site.register(Product,ProductAdmin)

