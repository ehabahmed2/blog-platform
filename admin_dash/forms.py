from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'is_active', 'is_staff', 'password1', 'password2']

    # Add custom styling for the checkboxes directly in the form
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'id': 'is_active'
    }))
    is_staff = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'id': 'is_staff'
    }))
