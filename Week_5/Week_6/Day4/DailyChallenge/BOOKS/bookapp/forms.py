from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from bookapp.models import BookReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['associated_book', 'review_text', 'rating', 'user']
        
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
