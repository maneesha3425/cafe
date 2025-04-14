from django.db import models

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('pizza', 'Pizza'),
        ('coffee', 'Coffee'),
        ('burger', 'Burger'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
        ('sandwich', 'Sandwich'),  # New category
        ('pasta', 'Pasta'),         # New category
        ('drink', 'Drink'),         # New category
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.URLField(null=True, blank=True)  # This field stores the URL of the image
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='pizza'  # Set default category here
    )

    def __str__(self):
        return self.name
