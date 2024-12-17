from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length = 32)
    author = models.CharField(max_length = 32)
    price = models.IntegerField()
    genre = models.CharField(max_length=32)
    quantity = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name