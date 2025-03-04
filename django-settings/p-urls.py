#overall project urls
from django.contrib import admin
from django.urls import path, include

# create array of url patters
urlpatters = [
    path('admin/', admin.sit.urls),
    path('authentication/', include('authentication.urls')),
]