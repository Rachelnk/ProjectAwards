from django.test import TestCase
from django.contrib.auth.models import User
from .models import Portfolio, Profile, Rating

# Create your tests here.

class TestUserProfile(TestCase):
    def setUp(self):
        self.new_user=User(first_name='John', last_name='Doe', username='user', email='user@gmail.com',password='user')
        self.new_user.save()

        self.profile=Profile(
            author=self.new_user, 
            bio='about me', 
            profile_image='profile.jpg',
            location = 'Kenya',
            personal_website = 'mysite.com',
            github_link = 'github.com',
            instagram_link = 'instagram.com',
            linkedin_link = 'linkedin.com',
            twitter_link = 'twitter.com'
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
