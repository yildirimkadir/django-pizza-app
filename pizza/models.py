from django.db import models

# Create your models here.
class Size(models.Model):
    title = models.CharField(("Size"), max_length=100)
    def __str__(self):
        return self.title 
    
 
class Pizza(models.Model):
    topping_1 = models.CharField(('Topping 1'), max_length=70)
    topping_2 = models.CharField(('Topping 2'), max_length=70)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.topping_1}, {self.topping_2}, {self.size}"