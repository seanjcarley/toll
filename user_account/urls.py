from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_user_profile, name='profile'),
    path('signup', views.create_user_profile, name='signup'),
]