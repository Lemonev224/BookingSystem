from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=200, null=True, default=False)
	lastname = models.CharField(max_length=200, null=True, default=False)
	email = models.CharField(max_length=200, default=False)

	def __str__(self):
		return self.fistname
	
	def __str__(self):
		return self.lastname


class Product(models.Model):
	name = models.CharField(max_length=200, default=False)
	models.CharField(max_length=140, null=True, default=False)
	price = models.FloatField(max_length=200)
	digital = models.BooleanField(default=False,null=True, blank=True)
	description = models.CharField(max_length=200, default='Place-Date')
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
	class Meta:
		verbose_name = "Workshops"
		verbose_name_plural = "Workshops"

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True, default=False)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 
	

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, default=False)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, default=False)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	
	class Meta:
		verbose_name = "Customer Bookings"
		verbose_name_plural = "Customer Bookings"

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False, default=False)
	tel = models.CharField(max_length=200, null=False, default=False)
	contact = models.CharField(max_length=200, null=False, default=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
	
	class Meta:
		verbose_name = "Customer Booking Information"
		verbose_name_plural = "Customer Booking Information"