from django.urls import path
from App import views
# app_name = 'App'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('events/', views.events, name = 'events'),
    path('music/', views.music, name = 'music'),
    path('team/', views.team, name = 'team'),
    path('booking/<int:pk>/', views.booking, name = 'booking'),
    path('contact/', views.contact, name = 'contact'),
    path('confirmation/', views.confirmation, name = 'confirmation'),
]