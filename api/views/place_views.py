from rest_framework import generics
from api.models import Listing
from api.serializers import places_serializers


class CreatePlaceView(generics.CreateAPIView):
    """Добавление места отдыха"""

    serializer_class = places_serializers.CreatePlacesSerializer


class DeletePlaceByIdView(generics.DestroyAPIView):
    """Удаление места отдыха по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = places_serializers.DeletePlaceSerializer


class UpdatePlaceByIdView(generics.UpdateAPIView):
    """Обновление места отдыха по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = places_serializers.UpdatePlaceSerializer


class GetPlaceView(generics.ListAPIView):
    """Вывод всех мест отдыха"""

    queryset = Listing.objects.filter(category=None)
    serializer_class = places_serializers.GetPlaceSerializer


class FindPlaceByIdView(generics.RetrieveAPIView):
    """Поиск места отдыха по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = places_serializers.GetPlaceSerializer
