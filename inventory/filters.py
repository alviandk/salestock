from django_filters import FilterSet, CharFilter, NumberFilter

from .models import Product

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
