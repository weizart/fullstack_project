from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name  # Return the name as the string representation


# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()  # Reference to dealer in Cloudant
    
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('SPORTS', 'Sports Car'),
        ('PICKUP', 'Pickup Truck'),
        ('VAN', 'Van'),
        ('MINIVAN', 'Mini Van'),
        ('CONVERTIBLE', 'Convertible'),
    ]
    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SEDAN')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"  # Return a descriptive string representation
