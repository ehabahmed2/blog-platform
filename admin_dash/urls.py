from django.urls import path
from . import views


urlpatterns = [
    path('', views.dash, name='dash'),
    path('register_author/', views.reg_author, name='reg_author'),
    path('manage_authors/', views.manage_authors, name='manage_authors'),
    path('logout/', views.logout_user, name='logout'),
]