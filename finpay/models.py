from django.db import models

# Create your models here.

# extend your user model to include age,gender,phone no, country ,amount , activation boolean 
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.IntegerField(null=True)

    height = models.IntegerField(null=True)

    country= models.CharField(max_length=255)

    activation= models.BooleanField(default=False)

    amount= models.FloatField(default=0)

    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.email}"



class Vcard(models.Model):
    CARD = (
        ('V','verve'),
        ('M','mastercard'),
        ('vi','visa')

    )
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    cardnumber = models.CharField(max_length=20)
    cvv = models.CharField(max_length=3)
    cardtype = models.CharField(max_length=3, choices=CARD) 
    expirydate = models.DateField()

    def __str__(self):
        return f"{self.user} {self.cardtype}"


