"""ionicserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api.resources import ProductResource
from api.resources import CategoryResource
from api.resources import OrderResource
from django.conf import settings
from django.conf.urls.static import static

product_resource = ProductResource()
category_resource = CategoryResource()
order_resource = OrderResource()

urlpatterns = [
    path('admin/', admin.site.urls),
path('api/',include(product_resource.urls)),
    path('api/',include(category_resource.urls)),
    path('api/',include(order_resource.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
