from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import Login


User = get_user_model()
class CreateUser(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class LoginUser(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(LoginUser, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    password = forms.CharField(widget=forms.PasswordInput())  # To display the password field as '*****' in forms

# update user profile
class UpdateProfile(UserChangeForm):
    password = None # to hide the Password-authan
    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def __init__(self, *args, **kwargs):
        super(UpdateProfile, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

