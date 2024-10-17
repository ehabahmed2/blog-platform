from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
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
        return self.user

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.get_or_create(user = instance)
        user_profile.save()



