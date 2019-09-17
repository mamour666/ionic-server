

from tastypie.resources import ModelResource
from .models import Product
from .models import Category
from .models import Order
from tastypie.authorization import Authorization



class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        authorization = Authorization()


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        authorization = Authorization()

class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
        authorization = Authorization()

