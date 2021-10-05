from rest_framework import generics
from api.models import Category
from api.serializers import category_serializers


class CreateCategoryView(generics.CreateAPIView):
    """Добавление категории"""

    serializer_class = category_serializers.CreateCategorySerializer


class DeleteCategoryByIdView(generics.DestroyAPIView):
    """Удаление категории по идентификации"""

    queryset = Category.objects.all()
    serializer_class = category_serializers.DeleteCategorySerializer


class UpdateCategoryByIdView(generics.UpdateAPIView):
    """Обновление категории по идентификации"""

    queryset = Category.objects.all()
    serializer_class = category_serializers.UpdateCategorySerializer


class GetCategoryView(generics.ListAPIView):
    """Вывод категорий"""

    queryset = Category.objects.filter(category=None)
    serializer_class = category_serializers.GetCategorySerializer


class FindCategoryByIdView(generics.RetrieveAPIView):
    """Поиск категории по идентификации"""

    queryset = Category.objects.all()
    serializer_class = category_serializers.GetCategorySerializer
