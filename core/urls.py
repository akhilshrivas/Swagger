from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is here
from home.swagger import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('home.urls')),  # This MUST be here to show your APIs
]