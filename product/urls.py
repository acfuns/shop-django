from django.urls import path, include
from rest_framework import routers

from .views import ProductListView, ProductDetailView, CategoryList, category_detail, ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:category_id>/products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('category_detail/<int:category_id>/', category_detail, name='category-detail'),
    path('', include(router.urls)),
]
