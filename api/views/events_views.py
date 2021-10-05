from rest_framework import generics
from api.models import Listing
from api.serializers import event_serializers


class CreateEventView(generics.CreateAPIView):
    """Добавление мероприятия"""

    serializer_class = event_serializers.CreateEventSerializers


class DeleteEventByIdView(generics.DestroyAPIView):
    """Удаление мероприятия по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = event_serializers.DeleteEventSerializer


class UpdateEventByIdView(generics.UpdateAPIView):
    """Обновление мероприятия по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = event_serializers.UpdateEventSerializer


class GetEventView(generics.ListAPIView):
    """Вывод всех мероприятии"""

    queryset = Listing.objects.filter(category=None)
    serializer_class = event_serializers.GetEventSerializer


class FindEventByIdView(generics.RetrieveAPIView):
    """Поиск мероприятия по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = event_serializers.GetEventSerializer
