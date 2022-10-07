from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_user_profile, name='profile'),
    path('vehicles', views.show_vehicles, name='vehicles'),
    path('signup', views.create_user_profile, name='signup'),
    path('vehicleinfo', views.get_vehicle_info, name='vehicleinfo'),
    path('checkusername', views.check_user_name, name='checkusername')
]
