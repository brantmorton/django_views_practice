from django.test import TestCase

from django.urls import reverse

import random

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Article

class TestArticleEndpoints(APITestCase):
    def setUp(self):
        self.article = Article.objects.create(title = 'Title 1', author = 'Han Solo', email = 'hsolo@gmail.com')

        self.article_data = {
            'title': self.article.title,
            'author': self.article.author,
            'email': self.article.email
        }

        self.detail_url = reverse('viewset-detail', args=[1])
        self.list_url = reverse('viewset-list')

    def test_get_article(self):
        response = self.client.get(self.detail_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == self.article.title
        assert response.data['author'] == self.article.author
        assert response.data['email'] == self.article.email


    def test_post_article(self):
        expected_articles = Article.objects.count() + 1
        response = self.client.get(self.list_url)
        assert Article.objects.count() == 1
        self.client.post(self.list_url, data=self.article_data)
        assert Article.objects.count() == expected_articles


    def test_put_article(self):
        expected_title = 'CHANGED'
        self.article_data['title'] = expected_title
        response = self.client.put(self.detail_url, data=self.article_data)
        assert response.data['title'] == expected_title
        assert Article.objects.first().title == expected_title

    def test_delete_article(self):
        expected_count = Article.objects.count() - 1
        response = self.client.delete(self.detail_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Article.objects.count() == expected_count

    
    def test_list_article(self):
        num_created = random.randint(5,10)
        expected_articles = Article.objects.count() + num_created
        for i in range(num_created):
            Article.objects.create(
                title=f'Title {i}',
                author=f'Brant Number {i}',
                email=f'email{i}@email.com'
            )

        response = self.client.get(self.list_url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == expected_articles


