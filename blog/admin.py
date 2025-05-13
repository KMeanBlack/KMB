from django.contrib import admin

# Register your models here.
from blog.models import *

admin.site.register((Post, BlogComment))
admin.site.register(Category)
admin.site.register(Tag)

