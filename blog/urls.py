from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # users
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('update-password/', views.update_pass, name='update_pass'),
    path('profile/', views.user_profile, name='user_profile'),
    #posts
    path('create-post/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post, name='post'),
    path('posts/', views.all_posts, name='posts'),
    path('manage-posts/', views.manage_posts, name='manage_posts'),
    path('edit-post/<int:pk>', views.edit_post, name='edit_post'),
    #categories
    path('categories', views.all_categories, name='all_categories'),
    path('categories/<int:pk>/', views.category_posts, name='category_posts'),
]
