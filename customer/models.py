from django.db import models
from django.urls import reverse

class SupplierList(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    contact = models.IntegerField()
    address = models.TextField(max_length=400, default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("list-detail", args=[str(self.id)])

class Orders(models.Model):

    order_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    number = models.IntegerField(default="")
    email = models.EmailField(max_length=254)
    address = models.TextField(max_length=400)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default="")
    zip = models.IntegerField()
    quantity = models.IntegerField()




