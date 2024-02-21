
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ccms/', include('ccms.urls')),
    # Custom 404 handler
    path('', HttpResponseNotFound),  # Return 404 for "/"
    path('favicon.ico', HttpResponseNotFound),  # Return 404 for "/favicon.ico"
]