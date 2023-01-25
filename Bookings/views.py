from django.shortcuts import render,redirect
from Adminapp.models import VenueList, Bookings
from Adminapp.forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url="SignIn")
def Booking(request,pk):
    Venue = VenueList.objects.filter(id = pk)
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get("Date")
            starttime = form.cleaned_data.get("start_time")
            endtime = form.cleaned_data.get("end_time")
            venue = VenueList.objects.get(id = pk)
            
            # validating date and time
            if Bookings.objects.filter(Date = date,venue = venue).exists():
                datavalue = Bookings.objects.filter(Date = date,venue = venue)
                for data in datavalue:
                    if data.start_time >= starttime and data.end_time <= starttime:
                        messages.info(request,"This Booking is not valid Slot is not avilable")
                        return redirect("Booking",pk=pk)
                    elif data.start_time >= starttime and data.end_time >= endtime and data.start_time <= endtime:
                        messages.info(request,"This Booking is not valid Slot is not avilable")
                        return redirect("Booking",pk=pk) 
                    elif data.start_time >= starttime and data.end_time <= endtime:
                        messages.info(request,"This Booking is not valid Slot is not avilable")
                        return redirect("Booking",pk=pk) 
                    elif data.start_time <= starttime and data.end_time >= endtime:
                        messages.info(request,"This Booking is not valid Slot is not avilable")
                        return redirect("Booking",pk=pk)
                    elif data.start_time <= starttime and data.end_time <= endtime and data.end_time >= starttime :
                        messages.info(request,"This Booking is not valid Slot is not avilable")
                        return redirect("Booking",pk=pk)
                    elif data.start_time >= endtime and data.end_time <= endtime:
                        messages.info(request,"This Booking is not valid Slot is not avilable")
                        return redirect("Booking",pk=pk)
                    else:
                        data = form.save()
                        data.Bookedby = request.user
                        data.venue = VenueList.objects.get(id = pk)
                        data.save()
                        messages.info(request,"Event Booked Succeess")
                        return redirect("Booking",pk=pk)
                        
                    
            #  end validation
            else:
                data = form.save()
                data.Bookedby = request.user
                data.venue = VenueList.objects.get(id = pk)
                data.save()
                messages.info(request,"Event Booked Succeess")
                return redirect("Booking",pk=pk)
            
            
    context = {
        "venue":Venue,
        "form":form
    }
    return render(request,'booking.html',context)

@login_required(login_url="SignIn")
def UserEventView(request):
    booking = Bookings.objects.filter(Bookedby = request.user)
    context = {
        "events":booking
    }
    return render(request,"usereventview.html", context)

@login_required(login_url="SignIn")
def ApproveBookingUser(request,pk):
    event = Bookings.objects.get(id = pk)
        
    if event.status == True:
        event.status = False
        event.save()
        
    return redirect('UserEventView')

@login_required(login_url="SignIn")
def DeleteBookingUser(request,pk):
    event = Bookings.objects.get(id = pk)
    event.delete()
    messages.info(request,"Item Deleted")
    return redirect('UserEventView')
