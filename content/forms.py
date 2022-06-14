from django import forms 
from django.contrib.auth.models import User
from .models import Portfolio, Profile, Rating
from cloudinary.forms import CloudinaryFileField

class AddPortfolioForm(forms.ModelForm):
    portfolio_image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Portfolio Title'}))
    caption = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control mb-4', 'rows': 5, 'placeholder':'Portfolio Description'}))
    category = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Portfolio Category i.e Professional'}))
    programming_language = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Programming Language'}))
    portfolio_site_url = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control mb-4', 'placeholder':'Project URL'}))
    repo_url = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control mb-4', 'placeholder':'GitHub Repository'}))

    class Meta:
      model = Portfolio
      fields = ['portfolio_image', 'title', 'caption', 'category', 'programming_language', 'portfolio_site_url', 'repo_url']

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UpdateProfileForm(forms.ModelForm):
    profile_image = CloudinaryFileField (label = '', options = { 'style': "margin-top: 30px",
      'tags': "directly_uploaded",
      'crop': 'limit', 'width': 1000, 'height': 1000,
      'eager': [{ 'crop': 'fill', 'width': 150, 'height': 100 }]
    })
    # profile_image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    profession = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Profession'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control mb-4', 'rows': 5}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'location'}))
    personal_website = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control mb-4', 'placeholder':'Link'}))
    github_link = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control mb-4', 'placeholder':'Link'}))
    instagram_link = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control mb-4', 'placeholder':'Link'}))
    linkedin_link = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control mb-4', 'placeholder':'Link'}))
    twitter_link = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control mb-4', 'placeholder':'Link'}))

    class Meta:
        model = Profile
        fields = ['profile_image', 'profession', 'bio', 'location', 'personal_website', 'github_link', 'instagram_link', 'linkedin_link', 'twitter_link']

class RatingForm(forms.ModelForm):
  usability = forms.IntegerField(required=True, label_suffix=" : ", min_value=1, max_value=10,widget=forms.NumberInput(attrs={'class': 'form-control mb-4', 'placeholder':'Usability Rating'}))

  design = forms.IntegerField(required=True, label_suffix=" : ", min_value=1, max_value=10,widget=forms.NumberInput(attrs={'class': 'form-control mb-4', 'placeholder':'Design Rating'}))

  content = forms.IntegerField(required=True, label_suffix=" : ", min_value=1, max_value=10,widget=forms.NumberInput(attrs={'class': 'form-control mb-4', 'placeholder':'Content Rating'}))

  class Meta:
      model = Rating
      fields = ['usability', 'design', 'content']
