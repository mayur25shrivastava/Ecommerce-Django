from pickle import TRUE
from pydoc import describe
from pyexpat import model
from django.db import models

# Create your models here.

class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=60)
    category= models.CharField(max_length=80, default="")
    sub_category= models.CharField(max_length=60, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=600)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name


# you have to do make migrations after making modals   -------------> python manage.py makemigrations
#then you have to do migrate  ------->python manage.py migrate

#after this register your modals in admin.py
#just by writting one line.

#then import it in views.py
#and use it

    #  contact models 

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    email= models.CharField(max_length=60, default="")
    phone= models.CharField(max_length=70, default="")
    desc=models.CharField(max_length=600, default="")
   
    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=4000)
    amount = models.IntegerField(default=0)
    name=models.CharField(max_length=80)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=75)
    state=models.CharField(max_length=75)
    zip_code=models.CharField(max_length=80)
    phone=models.CharField(max_length=80,default="")


class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=4000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."
