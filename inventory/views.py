from rest_framework import authentication, permissions, viewsets, filters
from rest_framework import filters
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse as api_reverse
from rest_framework.views import APIView

from .filters import ProductFilter, VariationFilter
from .models import Product, Category, Variation
from .pagination import ProductPagination, CategoryPagination
from .serializers import (
		CategorySerializer,
		ProductSerializer,
		VariationSerializer,
		)


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


class VariationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for POST, PUT, GET, PATCH and DELETE Variation."""
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer
    filter_class = VariationFilter


class ProductViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for POST, PUT, GET, PATCH and DELETE Products."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    search_fields = ('title',)
    ordering_fields = ('title',)


class CategoryViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for POST, PUT, GET, PATCH and DELETE Categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ('title', )
    ordering_fields = ('title',)
