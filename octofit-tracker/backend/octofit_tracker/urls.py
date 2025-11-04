from django.contrib import admin
from django.urls import path, include
from .api_urls import urlpatterns as api_urlpatterns

urlpatterns = [
	path('admin/', admin.site.urls),
	*api_urlpatterns,
]

