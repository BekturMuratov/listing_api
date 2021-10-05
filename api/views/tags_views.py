from rest_framework import generics
from api.models import Category
from api.serializers import tags_serializers


class CreateTagView(generics.CreateAPIView):
    """Добавление tag"""

    serializer_class = tags_serializers.CreateTagSerializer


class DeleteTagByIdView(generics.DestroyAPIView):
    """Удаление tag по идентификации"""

    queryset = Category.objects.all()
    serializer_class = tags_serializers.DeleteTagSerializer


class UpdateTagByIdView(generics.UpdateAPIView):
    """Обновление tag по идентификации"""

    queryset = Category.objects.all()
    serializer_class = tags_serializers.UpdateTagSerializer


class GetTagView(generics.ListAPIView):
    """Вывод tags"""

    queryset = Category.objects.filter(category=None)
    serializer_class = tags_serializers.GetTagSerializer


class FindTagByIdView(generics.RetrieveAPIView):
    """Поиск tags по идентификации"""

    queryset = Category.objects.all()
    serializer_class = tags_serializers.GetTagSerializer
