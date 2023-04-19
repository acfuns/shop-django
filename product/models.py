from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=60)
    description = models.TextField()
    category_img = models.ImageField(upload_to="img/%Y/%m/%d", default="default.png")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField()
    feature_age = models.IntegerField()
    feature_material = models.CharField(max_length=100)
    img = models.ImageField(upload_to="img/%Y/%m/%d", default="default.png")

    def __str__(self):
        return self.name
