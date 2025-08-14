# SmartDB/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # The URL for the Django admin interface.
    path('admin/', admin.site.urls),
    
    # This line tells Django to use the URL patterns in prototype/urls.py
    # to handle requests for the root path ('/').
    path('', include('prototype.urls')),
    
    # This path is a namespace for your API endpoints.
    # It routes all URLs starting with 'api/' to prototype/urls.py.
    path('api/', include('prototype.urls')),
]