from django.shortcuts import render,redirect
from .forms import UserAddForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .decorators import admin_only

from Adminapp.models import VenueList
# Create your views here.

@admin_only
def UserIndex(request):
    context = {
        "venues":VenueList.objects.all()
    }
    return render(request,"index.html",context)



def SignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('UserIndex')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('SignIn')
        
    return render(request,"login.html")
    # return render(request,"login.html")

def SignUp(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('SignUp')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('SignUp')
            else:
                new_user = form.save()
                new_user.save()
                # group = Group.objects.get(name='user')
                # new_user.groups.add(group) 
                messages.success(request,"User Created")
                return redirect('SignIn')
            
    return render(request,"register.html",{"form":form})

def SignOut(request):
    logout(request)
    return redirect('UserIndex')

def AllVenues(request):
    
    venues = VenueList.objects.all()
    context = {
        "venues":venues
    }
    
    return render(request,"allvenues.html",context)