
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from Public import urls
import Public
import Adminapp
from Adminapp import urls
import Bookings
from Bookings import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(Public.urls)),
    path("Adminapp/",include(Adminapp.urls)),
    path("Bookings/",include(Bookings.urls)),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
