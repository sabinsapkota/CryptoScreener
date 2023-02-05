from django.db import models
from datetime import datetime



# Create your models here.
class Crypto(models.Model):
    symbol = models.CharField(max_length=10)
    trend = models.CharField(max_length=25,null = True)
    price1 = models.FloatField(blank=True, null=True)
    price2 = models.FloatField(blank=True, null=True)
    price3 = models.FloatField(blank=True, null=True)
    price4 = models.FloatField(blank=True, null=True)
    price5 = models.FloatField(blank=True, null=True)
    price6 = models.FloatField()
    price7 = models.FloatField()
    price8 = models.FloatField()
    price9 = models.FloatField()
    price10 = models.FloatField()
    price11 = models.FloatField()
    price12 = models.FloatField()
    price13 = models.FloatField()




    
    def save(self, *args, **kwargs):
     if float(self.price10)>float(self.price9) >float(self.price8) >float(self.price7) >float(self.price6)>float(self.price5):
      self.trend = "5star"
     elif float(self.price10)>float(self.price9) >float(self.price8) >float(self.price7) >float(self.price6):
      self.trend = "4star"
     elif float(self.price10)>float(self.price9)>float(self.price8) >float(self.price7):
      self.trend = "3star"
     else:
        self.trend = "Bearish"
     super(Crypto, self).save(*args, **kwargs) # Call the "real" save() method.
 
    def __str__(self):
     return f"{self.symbol}"

