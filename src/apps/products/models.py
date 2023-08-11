from django.db import models
from ..users.models import User

class Category(models.Model):
    name = models.CharField("Name", max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField("Name", max_length=100)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products", null=True)
    tags = models.ManyToManyField(Tag, related_name="products")
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    created_at = models.DateField("Date created", auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name[:30]