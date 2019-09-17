from django.db import models

# Create your models here.

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/products/images', blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)


class Order(models.Model):
    date = models.CharField(max_length=100,blank=True,default=None)
    adresse = models.CharField(max_length=300)
    productQuantite = models.CharField(max_length=1000)
    productName = models.TextField(max_length=1000000000000)
    name = models.CharField(max_length=100,db_index=True,null=True,blank=True)

    class Meta:
        ordering = ('name',)

    # def __str__(self):
    #     if self.name == None:
    #         return "ERROR-CUSTOMER NAME IS NULL"
    #     return self.name

    def __str__(self):
        return (self.name)