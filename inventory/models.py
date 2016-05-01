from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify


class Category(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("category_detail", kwargs={"slug": self.slug })


class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	active = models.BooleanField(default=True)
	category = models.ForeignKey('Category', blank=True, null=True, related_name='product_category')


	class Meta:
		ordering = ["-title"]

	def __unicode__(self): #def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("product_detail", kwargs={"pk": self.pk})


def image_upload_to(instance, filename):
	title = instance.product.title
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
	return "products/%s/%s" %(slug, new_filename)


class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to=image_upload_to)

	def __unicode__(self):
		return self.product.title


class Variation(models.Model):
    product = models.ForeignKey(Product)
    color = models.CharField(max_length=120, null=True, blank=True)
    size = models.CharField(max_length=120, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(null=True, blank=True) #refer none == unlimited amount

    def __unicode__(self):
		return self.title

    def get_price(self):
		if self.sale_price is not None:
			return self.sale_price
		else:
			return self.price

    def get_absolute_url(self):
		return self.product.get_absolute_url()

    def get_title(self):
		return "%s -%s -%s" %(self.product.title, self.color, self.size)
