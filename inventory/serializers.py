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
			"color",
			"size",
			"price",
		]


class ProductSerializer(serializers.ModelSerializer):

	variation_set = VariationSerializer(many=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			"id",
			"title",
			"image",
			"variation_set",
		]

	def get_image(self, obj):
		try:
			return obj.productimage_set.first().image.url
		except:
			return None




class ProductDetailSerializer(serializers.ModelSerializer):
	variation_set = VariationSerializer(many=True, read_only=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			"id",
			"title",
			"description",
			"price",
			"image",
			"variation_set",
		]

	def get_image(self, obj):
		return obj.productimage_set.first().image.url


class ProductDetailUpdateSerializer(serializers.ModelSerializer):
	variation_set = VariationSerializer(many=True, read_only=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			"id",
			"title",
			"description",
			"price",
			"image",
			"variation_set",
		]

	def get_image(self, obj):
		try:
			return obj.productimage_set.first().image.url
		except:
			return None

	def create(self, validated_data):
		title = validated_data["title"]
		Product.objects.get(title=title)
		product = Product.objects.create(**validated_data)
		return product

	def update(self, instance, validated_data):
		instance.title = validated_data["title"]
		instance.save()
		return instance


class CategorySerializer(serializers.ModelSerializer):

    #product_set = ProductSerializer(many=True, read_only=True)

    class Meta:
		model = Category
		fields = [

			"id",
			"title",
			"description",
			#"product_set",

		]
