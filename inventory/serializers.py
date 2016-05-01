from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.reverse import reverse

from inventory.models import Category, Product, Variation


class VariationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Variation
		fields = [
			"id",
			"product",
			"color",
			"size",
			"price",
			"inventory",
		]

class VariationsetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Variation
		fields = [
			"id",
			"color",
			"size",
			"price",
			"inventory",
		]


class ProductSerializer(serializers.ModelSerializer):
	variation_set = VariationsetSerializer(many=True, read_only=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			"id",
			"category",
			"title",
			"image",
			"variation_set",
		]

	def get_image(self, obj):
		try:
			return obj.productimage_set.first().image.url
		except:
			return None


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
		model = Category
		fields = [
			"id",
			"title",
			"description",
		]
