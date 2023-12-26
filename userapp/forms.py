from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from socialmedia.models import UserProfile,Posts,Comments


class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]

class SignInForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=("user",)
        widgets={
            "dob":forms.DateInput(attrs={"type":"date"}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["title","post_image"]
        widgets={
            "post_image":forms.FileInput(attrs={"class":"form-control"})
        }

class UserSearchForm(forms.Form):
    username=forms.CharField()

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["text"]