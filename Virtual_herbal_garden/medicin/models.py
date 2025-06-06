from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Herb(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    description = RichTextField()
    image = models.CharField(max_length=300)
    date_added = models.DateField(auto_now_add=True)

class Add_herb(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='herbs/', blank=True, null=True) 


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Remedy(models.Model):
    disease = models.CharField(max_length=100, unique=True)
    herbs = models.ManyToManyField(Herb, related_name='remedies')

