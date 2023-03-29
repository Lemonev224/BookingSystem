
from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
   

]

admin.site.site_header = 'Andrea Naylor Art'              # default: "Django Administration"
admin.site.index_title = 'Andrea Naylor Art'                 # default: "Site administration"
admin.site.site_title = 'Admin' # default: "Django site admin"
