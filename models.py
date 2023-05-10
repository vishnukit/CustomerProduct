from django.db import models

class customer(models.Model):
    #objects = None
    customer_id=models.IntegerField()
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    phone=models.IntegerField()

    def __str__(self):
        return self.firstname

class products(models.Model):
    product_id = models.IntegerField()
    productname = models.CharField(max_length=20)
    expirydate = models.DateField()

    def __str__(self):
        return self.productname
