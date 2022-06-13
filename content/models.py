from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', null=True)
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


    # def save_profile(self):
    #     self.save()

    # def delete_profile(self):
    #     self.delete()

    # @classmethod
    # def search_profile(cls, name):
    #     return cls.objects.filter(user__username__icontains=name).all()
    
    
    def __str__(self):
      return str(self.id)
    
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    class Meta:
        verbose_name_plural = 'Profiles'

class Portfolio(models.Model):
    portfolio_image = CloudinaryField('image', null= True)
    title = models.CharField(max_length=500, verbose_name='Title', null=True)
    caption = models.CharField(max_length=2200, verbose_name='Caption', null=True)
    portfolio_site_url = models.URLField(max_length=500, verbose_name="Webiste Link", null=True, blank=True)
    repo_url = models.URLField(max_length=500, verbose_name="GitHub Repository", null=True)
    programming_language = models.CharField(max_length=500, verbose_name='Programming Language', null=True)
    category = models.CharField(max_length=500, verbose_name='Category', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', null = True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Profile', null =True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created', null= True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated', null= True)

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
      


