from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your models here.
from django.core.exceptions import ValidationError

class CustomUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email is required.")
        allowed_domain = "@example.com"
        if not email.endswith(allowed_domain):
            raise ValidationError(f"Email must be registered with the {allowed_domain} domain.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise ValidationError("Username is required.")
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password1")
    #     confirm_password = cleaned_data.get("password2")
        
    #     if password and confirm_password and password != confirm_password:
    #         raise forms.ValidationError("Passwords do not match!")
        
    #     return cleaned_data

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)