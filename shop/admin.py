from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Orders, OrderUpdate, Category, Sub_Category



admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)