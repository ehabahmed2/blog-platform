from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime
# Create your models here.
class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)

# User profile
User = get_user_model()
class UserProfile(models.Model):
    # inhirit user's info
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.save()

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='Category/imgs/%y/%m/%d', default='category/imgs/default.jpg')
    def __str__(self):
        return self.title

class CreatePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=900000)
    image = models.ImageField(upload_to='Posts/imgs/%y/%m/%d/', default='Posts/imgs/default.jpg')
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey(CreatePost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'


