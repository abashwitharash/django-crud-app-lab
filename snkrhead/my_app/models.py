from django.db import models

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='images/shoes/')

    def __str__(self):
        return self.name