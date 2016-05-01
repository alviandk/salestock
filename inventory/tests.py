from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from inventory.models import Category, Product, Variation

class CategoryTests(APITestCase):
    def test_create_category(self):
        """
        Ensure we can create a new category object.
        """
        user = User.objects.create(username='admin')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        url = reverse('category-list')
        data = {'title': 'Watch'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().title, 'Watch')
