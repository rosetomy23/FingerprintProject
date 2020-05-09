from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.hwhome, name='hwhome'),
    path('home/', views.home, name='home'),
    path('logout/', views.loggingout, name='logout'),
    path('clear/', views.clear, name='clear'),
    path('enroll/', views.enroll, name='enroll'),
    path('record/', views.record, name='record'),
]
