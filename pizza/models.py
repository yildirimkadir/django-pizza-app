from django.db import models

# Create your models here.
class Pizza(models.Model):
    topping_1 = models.CharField(('Topping 1'), max_length=70)
    topping_2 = models.CharField(('Topping 2'), max_length=70)
    SIZE = [
        ("1", "small"),
        ("2", "medium"),
        ("3", "large"),
    ]
    size = models.CharField('Size', max_length=2, choices=SIZE)
    
    def __str__(self):
        return f"{self.toping_1}, {self.toping_2}"