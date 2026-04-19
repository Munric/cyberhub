from django.db import models

class Service(models.Model):

    PRICE_TYPE = (
        ('fixed','Fixed'),
        ('per_page','Per Page'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    price_type = models.CharField(max_length=20, choices=PRICE_TYPE)
    requires_upload = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name