from django.urls import path
from.import views

urlpatterns = [
    path("Booking/<int:pk>",views.Booking,name="Booking"),
    path("UserEventView",views.UserEventView,name="UserEventView"),
    path("ApproveBookingUser/<int:pk>",views.ApproveBookingUser,name="ApproveBookingUser"),
    path("DeleteBookingUser/<int:pk>",views.DeleteBookingUser,name="DeleteBookingUser"),
    
]
