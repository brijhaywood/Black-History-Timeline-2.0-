from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('facts.urls', namespace='home')),
    path('api/', include('facts_api.urls', namespace='facts_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
