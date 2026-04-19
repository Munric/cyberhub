from django.db import models

# Create your models here.
from django.db import models
from orders.models import Order

class Payment(models.Model):

    STATUS = (
        ('success','Success'),
        ('failed','Failed'),
    )

    order = models.ForeignKey(Order,on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=15)

    amount = models.DecimalField(max_digits=8,decimal_places=2)

    mpesa_code = models.CharField(max_length=100,blank=True,null=True)

    status = models.CharField(max_length=20,choices=STATUS)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id}"
    
    mpesa_code = models.CharField(max_length=50, blank=True, null=True)