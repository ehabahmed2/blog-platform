from django.urls import path
from . import views


urlpatterns = [
    path('', views.dash, name='dash'),
    path('register-author/', views.reg_author, name='reg_author'),
    path('manage-authors/', views.manage_authors, name='manage_authors'),
    path('logout/', views.logout_user, name='logout'),
]