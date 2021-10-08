from rest_framework import generics
from api.models import Listing
from api.serializers import salons_serializers


class CreateSalonView(generics.CreateAPIView):
    """Добавление салона"""

    serializer_class = salons_serializers.CreateSalonSerializer


class DeleteSalonByIdView(generics.DestroyAPIView):
    """Удаление салона по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = salons_serializers.DeleteSalonSerializer


class UpdateSalonByIdView(generics.UpdateAPIView):
    """Обновление салона по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = salons_serializers.UpdateSalonSerializer


class GetSalonView(generics.ListAPIView):
    """Вывод всех салонов"""

    queryset = Listing.objects.filter(category=None)
    serializer_class = salons_serializers.GetSalonSerializer


class FindSalonByIdView(generics.RetrieveAPIView):
    """Поиск салона по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = salons_serializers.GetSalonSerializer
