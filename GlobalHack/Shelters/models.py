from django.db import models
from geopy.geocoders import GoogleV3
# Create your models here.
class Shelter(models.Model):
    Name = models.CharField(max_length=200,default="")
    Address = models.CharField(max_length=100);
    Phone = models.CharField(max_length=100);
    Email = models.EmailField(max_length=100);
    Specialty = models.CharField(max_length=100);
    maxCap = models.IntegerField(default = 0);
    foodAvailable = models.NullBooleanField()
    shelterAvailable = models.NullBooleanField()
    hygenicAvailable = models.NullBooleanField()
    counselingAvailable = models.NullBooleanField()
    otherAvailable = models.NullBooleanField()
    otherDetails = models.CharField(max_length=500,blank=True)
    latitude = models.DecimalField(max_digits=9,decimal_places=6)
    longitude = models.DecimalField(max_digits=9,decimal_places=6)


def MakeShelter(Values):
    s = Shelter()
    s.Name = Values['Name'];
    s.Address = Values['Address']
    s.Phone = Values['Contact']
    s.Email = Values['ContactE']
    
    if 'Specialty' in Values:
        s.Specialty = Values['name'];
    
    if 'maxCap' in Values:
        if not 'shelterAvailable' in Values:
            return False
        s.maxCap = Values['maxCap']
    
    s.foodAvailable = 'foodAvailable' in Values
    
    s.shelterAvailable = 'shelterAvailable' in Values
    
    if s.shelterAvailable and 'maxCap' not in Values:
        return False

    s.hygenicAvailable = 'hygenicAvailable' in Values

    s.counselingAvailable = 'counselingAvailable' in Values
    
    s.otherAvailable = 'otherAvailable' in Values;
    
    if 'otherDetails' in  Values:
        s.otherDetails = Values['otherDetails']
    
    g = GoogleV3()
    g = g.geocode(s.Address)
    s.latitude = g.latitude
    s.longitude = g.longitude
    s.save();
    return True
