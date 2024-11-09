from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(max_length=50, choices=[
        ('fruit', 'Fruit'),
        ('vegetable', 'Vegetable'),
        ('herb', 'Herb')
    ])
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

