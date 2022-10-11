from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
import uuid

# https://bitbucket.org/machax/workspace/snippets/qX54n4/backend-assignment
# Create your models here.

class kredilyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    #can add extra fields

    
class Product(models.Model):

    uuid = models.UUIDField(primary_key= True , default = uuid.uuid4 , editable=False)
    name = models.CharField(max_length = 50 , null = False)
    price = models.IntegerField(null = False)
    quantity = models.IntegerField(null = False)
    createdAt = models.DateTimeField(auto_now = True)
    upatedAt = models.DateTimeField()

class Order(models.Model):
    order_id = models.UUIDField(primary_key= True , default = uuid.uuid4 , editable=False)
    user = models.ForeignKey(kredilyUser , on_delete=models.CASCADE)
    # products = ArrayField(models.ForeignKey(Product , on_delete=models.CASCADE))
    products = ArrayField(base_field = models.CharField(max_length = 50))
    createdAt = models.DateTimeField(auto_now = True)
    upatedAt = models.DateTimeField() 