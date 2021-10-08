from rest_framework import generics
from api.models import Listing
from api.serializers import cars_serializers


class CreateCarView(generics.CreateAPIView):
    """Добавление автомобиля"""

    serializer_class = cars_serializers.CreateCarsSerializer


class DeleteCarByIdView(generics.DestroyAPIView):
    """Удаление автомобиля по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = cars_serializers.DeleteCarsSerializer


class UpdateCarByIdView(generics.UpdateAPIView):
    """Обновление автомобиля по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = cars_serializers.UpdateCarsSerializer


class GetCarView(generics.ListAPIView):
    """Вывод всех автомобилей"""

    queryset = Listing.objects.filter(category=None)
    serializer_class = cars_serializers.GetCarsSerializer


class FindCarByIdView(generics.RetrieveAPIView):
    """Поиск автомобиля по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = cars_serializers.GetCarsSerializer
