from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('upload/', include('uploadapp.urls')),
    path('', launchwaiting, name='launchhome'),
    path('admin/', admin.site.urls),
    path('upload/', include('uploadapp.urls')),
    path('report/', include('reports.urls')),
    path('hardware/', include('arduinopgm.urls')),
]
