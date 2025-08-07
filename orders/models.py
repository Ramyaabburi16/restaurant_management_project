from django.db import models
from django.contrib.auth.models import User
from products.models import Menu

class Order(models.Model):
    STSTUS_CHOICES = [
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('DELIVERED','Delivered'),
        ('CANCELLED','Cancelled'),
    ]

    customer = models.Foreignkey(User , on.delete=models.CASCADE)
    items = models.ManyToManyField(Menu)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField( max_length=10 , choices=STSTUS_CHOICES, default ='PENDING')
    created_at = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return f"Order#{self.id} - {self.customer.username}"