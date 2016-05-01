from django_filters import FilterSet, CharFilter, NumberFilter

from .models import Product, Variation

class ProductFilter(FilterSet):
	color = CharFilter(name='variation__color', lookup_type='icontains', distinct=True)
	size = CharFilter(name='variation__size', lookup_type='icontains', distinct=True)
	min_price = NumberFilter(name='variation__price', lookup_type='gte', distinct=True)
	max_price = NumberFilter(name='variation__price', lookup_type='lte', distinct=True)
	class Meta:
		model = Product
		fields = (
			'min_price',
			'max_price',
            'size',
            'color',
		)

class VariationFilter(FilterSet):
	color = CharFilter(name='color', lookup_type='icontains', distinct=True)
	size = CharFilter(name='size', lookup_type='icontains', distinct=True)
	min_price = NumberFilter(name='price', lookup_type='gte', distinct=True)
	max_price = NumberFilter(name='price', lookup_type='lte', distinct=True)
	class Meta:
		model = Variation
		fields = (
			'min_price',
			'max_price',
            'size',
            'color',
		)
