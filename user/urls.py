from django.urls import path
from user import views
urlpatterns = [
    path('register/',views.registerCustomer, name='register'),
    path('login/', views.loginCustomer, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    
]