from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', null=True)
    profile_pic = CloudinaryField('image')
    bio = models.TextField()
    username = models.CharField(max_length=60)
    profession = models.CharField(max_length=150, verbose_name='Profession', null=True, blank=True)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created, ', null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    personal_website = models.URLField(max_length=500, verbose_name="Personal Website", null=True, blank=True)
    github_link = models.URLField(max_length=500, verbose_name="GitHub Link", null=True, blank=True)
    instagram_link = models.URLField(max_length=500, verbose_name="Instagram Link", null=True, blank=True)
    linkedin_link = models.URLField(max_length=500, verbose_name="LinkedIn Link", null=True, blank=True)
    twitter_link = models.URLField(max_length=500, verbose_name="Twitter Link", null=True, blank=True)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    # @classmethod
    # def search_profile(cls, name):
    #     return cls.objects.filter(user__username__icontains=name).all()
    
    
    def __str__(self):
      return str(self.user)

    class Meta:
        verbose_name_plural = 'Profiles'

class Portfolio(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    photo = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
      return str(self.title)

    def save_portfolio(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def search_post(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_portfolio(cls):
        return cls.objects.all()
    
    class Meta:
        verbose_name_plural = 'Portfolios'

class Rating(models.Model):
    comment = models.CharField(max_length=2200, verbose_name='Comment', null=False)
    design_rating = models.IntegerField(default=0, null=False)
    usability_rating = models.IntegerField(default=0, null=False)
    content_rating = models.IntegerField(default=0, null=False)
    avarage_rating = models.IntegerField(default=0, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Profile')
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def _str_(self):
        return self.portfolio.title

    class Meta:
        verbose_name_plural = 'Ratings'
      


