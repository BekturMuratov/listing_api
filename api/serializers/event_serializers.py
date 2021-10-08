from rest_framework import serializers

from api.models import Listing


class CreateEventSerializers(serializers.ModelSerializer):
    """Добавления мероприятия """

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'category',
            'slug',
            'health_and_safety_measures',
            'location',
            'image',
            'thumbnail',
            'phone',
            'social_networks',
            'price',
        ]

class DeleteEventSerializer(serializers.ModelSerializer):
    """Удаление мероприятия по идентификации"""

    class Meta:
        model = Listing
        fields = '__all__'

class UpdateEventSerializer(serializers.ModelSerializer):
    """Обновление мероприятия по идентификации"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'category',
            'slug',
            'health_and_safety_measures',
            'location',
            'image',
            'thumbnail',
            'phone',
            'social_networks',
            'price',
        ]

class GetEventSerializer(serializers.ModelSerializer):
    """Вывод всех мероприятии"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'category',
            'slug',
            'health_and_safety_measures',
            'location',
            'image',
            'thumbnail',
            'phone',
            'social_networks',
            'price',
        ]
