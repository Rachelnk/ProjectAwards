from django.test import TestCase
from django.contrib.auth.models import User
from .models import Portfolio, Profile, Rating

# Create your tests here.

class TestUserProfile(TestCase):
    def setUp(self):
        self.new_user=User(first_name='ray', last_name='kiarie', username='user', email='user@gmail.com',password='123')
        self.new_user.save()

        self.profile=Profile(
            author=self.new_user, 
            bio='about me', 
            profile_pic ='profile.jpg',
            location = 'Kenya',
            personal_website = 'mysite.com',
            github_link = 'github.com',
            instagram_link = 'instagram.com',
            linkedin_link = 'linkedin.com',
            twitter_link = 'twitter.com'
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

class PortfolioTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="ray",
            first_name="ray",
            last_name="kiarie",
            email="rayray@gmail.com"
        )

        self.portfolio = Portfolio(
            portfolio_image = "default.jpg",
            title="Project",
            caption="Test Caption",
            portfolio_site_url="url.com",
            repo_url="github.com",
            programming_language="python",
            category="for practice",
            author=user,
            profile = user.profile
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.portfolio, Portfolio))

    def test_save_method(self):
          self.portfolio.save_portfolio()
          Portfolios = Portfolio.objects.all()
          self.assertTrue(len(Portfolios) > 0)

    def test_update_portfolio(self):
        self.portfolio.save_portfolio()
        Portfolios = Portfolio.objects.all()
        self.assertTrue(len(Portfolios) > 0)

    def test_delete_method(self):
        self.portfolio.save_portfolio()
        self.portfolio.delete()
        Portfolios = Portfolio.objects.all()
        self.assertTrue(len(Portfolios) == 0)