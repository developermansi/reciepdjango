from django.db import models

class recipes(models.Model):
    recipes_name = models.CharField(max_length=100)
    recipes_description = models.CharField(max_length=100)
    recipes_image = models.CharField(max_length=100)
