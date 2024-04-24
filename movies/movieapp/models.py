from django.db import models

# Create your models here.



class Contain(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=55)
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    aktif = models.BooleanField(default=True)
    writer = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
