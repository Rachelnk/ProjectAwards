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

