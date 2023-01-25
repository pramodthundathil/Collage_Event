from django.db import models
from django.contrib.auth.models import User


class VenueList(models.Model):
    
    Venue_Name = models.CharField(max_length=255)
    Seat_Numbers = models.CharField(max_length=255)
    Price = models.CharField(max_length=255)
    Venue_Discription = models.CharField(max_length=1000)
    Venue_Image = models.ImageField(upload_to="venue_image")
    addedby = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return str("{} {} seats".format(self.Venue_Name,self.Seat_Numbers))
    
class Bookings(models.Model):
    
    
    Name = models.CharField(max_length=255)
    Phone_number = models.CharField(max_length=255)
    Bookedby = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    venue = models.ForeignKey(VenueList,on_delete=models.CASCADE,null=True,blank=True)
    Date = models.DateField(auto_now_add=False)
    start_time = models.TimeField(auto_now_add=False)
    end_time = models.TimeField(auto_now_add=False)
    status = models.BooleanField(default=False)
    event_discription = models.CharField(max_length=255)
    # Name = models.CharField(max_length=255)
    # Phone_number = models.CharField(max_length=255)
    # Bookedby = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
