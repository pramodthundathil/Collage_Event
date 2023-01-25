from django.shortcuts import render,redirect
from .forms import VenueAddForm
from django.contrib import messages
from .models import VenueList, Bookings
from django.contrib.auth.decorators import login_required


@login_required(login_url="SignIn")
def EventMgrIndex(request):
    
    context = {
        'numberofevents':VenueList.objects.all().count(),
        "numberofbookings": Bookings.objects.all().count()
    }
    return render(request,'adminindex.html',context)

@login_required(login_url="SignIn")
def VenueViewAdmin(request):
    Venues = VenueList.objects.all()
    context = {
        'venues':Venues
    }
    return render(request,"adminvenueview.html",context)

@login_required(login_url="SignIn")
def EventViewAdmin(request):
    events = Bookings.objects.all()
    context = {
        "events":events
    }
    return render(request,"admineventview.html",context)

@login_required(login_url="SignIn")
def Addvenue(request):
    form = VenueAddForm()
    if request.method == "POST":
        form = VenueAddForm(request.POST,request.FILES)
        if form.is_valid():
            venue = form.save()
            venue.addedby = request.user
            venue.save()
            messages.info(request,"New Venue added")
            return redirect('Addvenue')
    
    return render(request,"addvenue.html",{"form":form})

@login_required(login_url="SignIn")
def ViewVenue(request,pk):
    venues = VenueList.objects.filter(id = pk)
    if request.method == "POST":
        venue = VenueList.objects.get(id = pk)
        
        name = request.POST["venue_name"]
        Snumber = request.POST["seat_num"]
        price = request.POST['price']
        dis = request.POST['dis']
        image = request.FILES['img']
        
        venue.Venue_Image.delete()
        venue.Venue_Image = image
        venue.Venue_Name  = name
        venue.Venue_Discription = dis
        venue.Seat_Numbers = Snumber
        venue.Price = price
        venue.save()
        
        messages.info(request,"Value updated")
        return redirect("ViewVenue", pk=pk)
    
    context = {
        "venues":venues
    }
    return render(request,"venuesingleview.html",context)

@login_required(login_url="SignIn")
def DeleteVenue(request,pk):
    venue = VenueList.objects.get(id = pk)
    venue.delete()
    messages.info(request,"Item Deleted")
    return redirect("VenueViewAdmin")
       
@login_required(login_url="SignIn")
def ApproveBooking(request,pk):
    event = Bookings.objects.get(id = pk)
    
    if event.status == False:
        event.status = True
        event.save()
        
    elif event.status == True:
        event.status = False
        event.save()
        
    return redirect('EventViewAdmin')

@login_required(login_url="SignIn")
def DeleteBooking(request,pk):
    event = Bookings.objects.get(id = pk)
    event.delete()
    messages.info(request,"Item Deleted")
    return redirect('EventViewAdmin')
    

