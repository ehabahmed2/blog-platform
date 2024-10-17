from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('update_password/', views.update_pass, name='update_pass'),
    path('profile/', views.user_profile, name='user_profile'),
]
