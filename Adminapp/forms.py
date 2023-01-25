from django.forms import ModelForm
from .models import VenueList,Bookings
from django.forms import TextInput,PasswordInput


class VenueAddForm(ModelForm):
    class Meta:
        model = VenueList
        fields = ["Venue_Name","Seat_Numbers","Price","Venue_Discription","Venue_Image"]
        
class BookingForm(ModelForm):
    class Meta:
        model = Bookings
        fields = ["Name","Phone_number","Date","start_time","end_time","event_discription"]

        widgets = {
            'Name':TextInput(attrs={"placeholder":"Organazation Name"}),
            'Phone_number': TextInput(attrs={"type":"number","placeholder":"Phone Number"}),
            'Date': TextInput(attrs={"type":"date"}),
            'start_time': TextInput(attrs={"type":"time"}),
            "end_time": TextInput(attrs={"type":"time"}),
            'event_discription':TextInput(attrs={"placeholder":"Event Details"})

        }
        
        