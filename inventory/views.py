from rest_framework import authentication, permissions, viewsets, filters
from rest_framework import filters
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse as api_reverse
from rest_framework.views import APIView

from .filters import ProductFilter
from .models import Product, Category
from .pagination import ProductPagination, CategoryPagination
from .serializers import (
		CategorySerializer,
		ProductSerializer,
		 ProductDetailSerializer,
		 ProductDetailUpdateSerializer
		)


class APIHomeView(APIView):

	def get(self, request, format=None):
		data = {

			"products": {
				"count": Product.objects.all().count(),
				"url": api_reverse("products_api", request=request)
			},
			"categories": {
				"count": Category.objects.all().count(),
				"url": api_reverse("categories_api", request=request)
			},

		}
		return Response(data)


class CategoryListAPIView(generics.ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	pagination_class = CategoryPagination


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	filter_backends = [
					filters.SearchFilter,
					filters.OrderingFilter,
					filters.DjangoFilterBackend
					]
	search_fields = ["title", "description"]
	ordering_fields  = ["title", "id"]
	filter_class = ProductFilter
	pagination_class = ProductPagination


class ProductRetrieveAPIView(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductDetailSerializer


class DefaultsMixin(object):
	"""Default settings for view authentication, permissions,
	filtering and pagination"""

	authentication_classes = (
	    authentication.BasicAuthentication,
	    authentication.TokenAuthentication,
	    authentication.SessionAuthentication
	)

	permission_classes =(
	    permissions.IsAuthenticatedOrReadOnly,
	)

	paginate_by = 25
	paginate_by_param = 'page_size'
	max_paginate_by = 100

	filter_backends = (
	    filters.DjangoFilterBackend,
	    filters.SearchFilter,
	    filters.OrderingFilter,
	)


class ProductViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Products."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    search_fields = ('title',)
    ordering_fields = ('title',)


class CategoryViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ('title', )
    ordering_fields = ('title',)
