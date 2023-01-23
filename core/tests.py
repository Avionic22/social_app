from django.test import TestCase
from core.models import User, Profile, Post, LikePost, FollowersCount

# Create your tests here.


class URLTests(TestCase):
    def test_testhomopage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_signinpage(self):
        response = self.client.get('/signin')
        self.assertEqual(response.status_code, 200)

    def test_signuppage(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200) 

    def test_settings(self):
        response = self.client.get('/settings')
        self.assertEqual(response.status_code, 302) 
    
    def test_logout(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302) 
        
    def test_upload(self):
        response = self.client.get('/upload')
        self.assertEqual(response.status_code, 302) 

    def test_like_post(self):
        response = self.client.get('/like-post')
        self.assertEqual(response.status_code, 302) 
        
    def test_profile(self):
        response = self.client.get('/profile/mark')
        self.assertEqual(response.status_code, 302) 

    def test_follow(self):
        response = self.client.get('/follow')
        self.assertEqual(response.status_code, 302) 

    def test_search(self):
        response = self.client.get('/search')
        self.assertEqual(response.status_code, 302) 


