from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'message', 'description', 'product_count', 'category_img')

    def get_product_count(self, obj):
        return obj.product_set.count()


class ProductSerializer(serializers.ModelSerializer):
    category_msg = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'price', 'stock', 'feature_age', 'feature_material', 'img',
                  'category_msg')
