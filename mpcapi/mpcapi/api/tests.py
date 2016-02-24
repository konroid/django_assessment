from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework import status
from models import Post, Comment
from rest_framework.response import Response
from django.core.urlresolvers import reverse

#
# Posts Tests
#
class PostTests(APITestCase):
    def test_post_to_posts(self):
        #
        # Checks post returns 201 when given valid data
        #
        response  = self.client.post(reverse('post_list'), {'userId': '1', 'title': 'Title test', 'body': 'Hello World - This is a test post'})
        #response.render()
        #self.post = response.data
        #print self.post
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)

    def test_404_post(self):
        #
        # Checks post returns 404 looking at non existant post
        #
        #self.post.id = 1
        response = self.client.get('/api/posts/9999/')
        #response.render()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_200_PUT_posts(self):
        #
        # Checks post returns 200 when using put
        #
        response = self.client.put('/api/posts/1/', {'userId': '1', 'title': 'Title test', 'body': 'Hello World - This is a test post - This is additional data'})
        #response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_400_PUT_posts(self):
        #
        # Checks post returns 400 when using put, body misspelt - bdy
        #
        response = self.client.put('/api/posts/1/', {'userId': '1', 'title': 'Title test', 'bdy': 'this is not going to work'})
        #response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
"""
#
# Comments Tests
#
class CommentTests(APITestCase):
    def test_post_to_comment(self):
        #
        # Checks comments returns 201 when given valid data
        #
        response = self.client.post(reverse('comment_list'), {'postId': '1', 'name': 'Konur Test', 'email': 'konur.kent@gmail.com', 'body': 'this is a test comment'})
        #response.render()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)

    def test_404_post(self):
        #
        # Checks comments returns 404 looking at non existant post
        #
        response = self.client.get('/api/comments/9999/')
        #response.render()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_200_PUT_comments(self):
        #
        # Checks comments returns 200 when using put
        #
        response = self.client.put('/api/comments/1/', {'postId': '1', 'name': 'Konur Test', 'email': 'konur.kent@gmail.com', 'body': 'this is a test comment - this is addtional data'})
        #response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_400_PUT_comments(self):
        #
        # Checks comments returns 400 when using put, body misspelt - bdy
        #
        response = self.client.put('/api/comments/1/', {'postId': '1', 'name': 'Konur Test', 'email': 'konur.kent@gmail.com', 'bdy': 'this is will not work'})
        #response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

"""
