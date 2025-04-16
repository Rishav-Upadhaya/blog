from django import forms
from .models import Post, CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create the add
class add_post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

    # def clean_email(self):
    #     title = self.cleaned_data.get('title')
    #     print(title)
    #     if "rough" in title:
    #         raise forms.ValidationError("Invalid title: spam detected!")
    #     return title

        

# class RegistrationForm(forms.Form):
#     username = forms.CharField(max_length=30)
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
        
#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError("Passwords do not match!")
        
#         return cleaned_data

