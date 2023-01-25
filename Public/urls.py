from django.urls import path
from .import views

urlpatterns = [
    path("",views.UserIndex,name="UserIndex"),
    path("SignIn",views.SignIn,name="SignIn"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("AllVenues",views.AllVenues,name="AllVenues"),
     
]
