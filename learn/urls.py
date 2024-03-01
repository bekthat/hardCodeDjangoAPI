from django.urls import path
from .views import ProductList, LessonList

urlpatterns = [
    path('api/products/', ProductList.as_view(), name='product-list'),
    path('api/products/<int:product_id>/lessons/', LessonList.as_view(), name='lesson-list'),
]
