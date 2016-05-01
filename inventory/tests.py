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
        self.client = APIClient()
        user = User.objects.create(username='admin')
        self.client.force_authenticate(user=user)
        url = reverse('category-list')
        data = {'title': 'Watch'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().title, 'Watch')


class ProductTests(APITestCase):
    def test_create_category(self):
        """
        Ensure we can create a new category object.
        """
        self.client = APIClient()
        user = User.objects.create(username='admin')
        self.client.force_authenticate(user=user)
        url = reverse('product-list')
        category = Category.objects.create(title='Watch')
        data = {'title': 'Swiss-Army', 'category': category.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().title, 'Swiss-Army')


class VariationTests(APITestCase):
    def test_create_category(self):
        """
        Ensure we can create a new category object.
        """
        self.client = APIClient()
        user = User.objects.create(username='admin')
        self.client.force_authenticate(user=user)
        url = reverse('variation-list')
        product = Product.objects.create(title='Swiss-Army')
        data = {'product': product.id, 'color': 'Gold', 'price': 40.00 }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Variation.objects.count(), 1)
        self.assertEqual(Variation.objects.get().color, 'Gold')
        self.assertEqual(Variation.objects.get().price, 40.00)
        
