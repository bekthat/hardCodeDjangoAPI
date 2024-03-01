from rest_framework import generics
from .models import Product, Lesson
from .serializers import ProductSerializer, LessonSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonList(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        return Lesson.objects.filter(product_id=self.kwargs['product_id'])
