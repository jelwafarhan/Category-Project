from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.
def get_file_path(request,filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)

class Category(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=get_file_path,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model): #applying Many to One Relationship
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=get_file_path,null=True,blank=True)
    small_description = models.CharField(max_length=250,null=False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    price = models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)



    def __str__(self):
        return self.name
