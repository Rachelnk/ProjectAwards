from django import forms 
from django.contrib.auth.models import User
from .models import Post, Profile, Rating

class AddPortfolioForm(forms.ModelForm):
    portfolio_image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Portfolio Title'}))
    caption = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control mb-4', 'rows': 5, 'placeholder':'Portfolio Description'}))
    category = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Portfolio Title'}))
    primary_language = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Portfolio Title'}))
    portfolio_site_url = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control mb-4', 'placeholder':'Portfolio URL'}))
    repo_url = forms.URLField(required=True, widget=forms.URLInput(attrs={'class': 'form-control mb-4', 'placeholder':'GitHub Repository'}))