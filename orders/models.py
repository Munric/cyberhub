from django.db import models
from services.models import Service

# ✅ DEFINE FIRST
STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('paid', 'Paid'),
    ('completed', 'Completed'),
]

class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    details = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service.name}"