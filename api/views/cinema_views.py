from rest_framework import generics
from api.models import Listing
from api.serializers import cinema_serializers


class CreateCinemaView(generics.CreateAPIView):
    """Добавление кинотеатра"""

    serializer_class = cinema_serializers.CreateCinemaSerializer


class DeleteCinemaByIdView(generics.DestroyAPIView):
    """Удаление кинотеатра по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = cinema_serializers.DeleteCinemaSerializer


class UpdateCinemaByIdView(generics.UpdateAPIView):
    """Обновление кинотеатра по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = cinema_serializers.UpdateCinemaSerializer


class GetCinemaView(generics.ListAPIView):
    """Вывод кинотеатров"""

    queryset = Listing.objects.filter(category=None)
    serializer_class = cinema_serializers.GetCinemaSerializer


class FindCinemaByIdView(generics.RetrieveAPIView):
    """Поиск кинотеатра по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = cinema_serializers.GetCinemaSerializer
