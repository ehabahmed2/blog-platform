from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # users
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('update_password/', views.update_pass, name='update_pass'),
    path('profile/', views.user_profile, name='user_profile'),
    #posts
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post, name='post'),

]
