from django.test import TestCase
from core.models import Profile, Post, LikePost, FollowersCount
from django.contrib.auth.models import User


class TestAppModels(TestCase):

    def setUp(self):
        user = User.objects.create(username="John", email="email@gmail.com", password="1234")
        self.user_profile = Profile.objects.create(user=user, id_user=1)
        self.user_post = Post.objects.create(user="John", caption="nice picture")
        self.like_post = LikePost.objects.create(post_id=1, username="John")
        self.followers_count = FollowersCount.objects.create(follower="Steve", user="John")


    def test_model_str(self):
        self.assertEqual(self.user_profile.__str__(), "John")
        self.assertEqual(self.user_post.__str__(), "John")
        self.assertEqual(self.like_post.__str__(), "John")
        self.assertEqual(self.followers_count.__str__(), "John")
        

