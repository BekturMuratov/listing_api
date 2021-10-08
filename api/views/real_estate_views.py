from rest_framework import generics
from api.models import Listing
from api.serializers import real_estate_serializers


class CreateRealEstateView(generics.CreateAPIView):
    """Добавление квартиры"""

    serializer_class = real_estate_serializers.CreateRealEstateSerializer


class DeleteRealEstateByIdView(generics.DestroyAPIView):
    """Удаление квартиры по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = real_estate_serializers.DeleteRealEstateSerializer


class UpdateRealEstateByIdView(generics.UpdateAPIView):
    """Обновление квартиры по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = real_estate_serializers.UpdateRealEstateSerializer


class GetRealEstateView(generics.ListAPIView):
    """Вывод квартиры"""

    queryset = Listing.objects.filter(category=None)
    serializer_class = real_estate_serializers.GetRealEstateSerializer


class FindRealEstateByIdView(generics.RetrieveAPIView):
    """Поиск квартиры по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = real_estate_serializers.GetRealEstateSerializer
