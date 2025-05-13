from django.db import models
from unicodedata import category, name
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.category.main_category.name + " -- " + self.category.name + " -- " + self.name


class Product(models.Model):
    product_id=models.AutoField
    Availability = models.IntegerField(null=True)
    product_name=models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    sub_category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    Product_information = RichTextField(null=True)
    desc = RichTextField(null=True)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
 

class Product_Image(models.Model):
    product = models.ForeignKey(Product, default=True, on_delete=models.CASCADE)
    Image_url = models.CharField(max_length=200)

class Additional_Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)


class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email= models.CharField(max_length=70, default="")
    phone= models.CharField(max_length=70, default="")
    desc=models.CharField(max_length=500, default="")
    

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone = models.CharField(max_length=13, default="")

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."