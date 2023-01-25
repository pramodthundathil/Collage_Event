from django.urls import path
from .import views

urlpatterns = [
    path("VenueViewAdmin",views.VenueViewAdmin,name="VenueViewAdmin"),
    path("EventViewAdmin",views.EventViewAdmin,name="EventViewAdmin"),
    path("Addvenue",views.Addvenue,name="Addvenue"),
    path("EventMgrIndex",views.EventMgrIndex,name="EventMgrIndex"),
    path("ApproveBooking/<int:pk>",views.ApproveBooking,name="ApproveBooking"),
    path("DeleteBooking/<int:pk>",views.DeleteBooking,name="DeleteBooking"),
    path("ViewVenue/<int:pk>",views.ViewVenue,name="ViewVenue"),
    path("DeleteVenue/<int:pk>",views.DeleteVenue,name="DeleteVenue")
    
]
