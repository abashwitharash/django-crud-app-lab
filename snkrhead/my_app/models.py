from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='images/shoes/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('snkr-detail', kwargs={'snkr_id': self.id}) 
    
class Cleaning(models.Model):
        date = models.DateField('Date Cleaned')

        shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

        def __str__(self):
            return f"{self.date}"
        
        class Meta:
             ordering = ['-date']