from rest_framework import serializers

from api.models import Listing

class CreateCinemaSerializer(serializers.ModelSerializer):
    """Добавление кинотеатра"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'cinema_features',
            'phone',
            'location',
            'price',
            'social_networks',
            'amenities',
            'category',
            'health_and_safety_measures',
            'email',
        ]

class DeleteCinemaSerializer(serializers.ModelSerializer):
    """Удаление кинотеатра по идентификации"""

    class Meta:
        model = Listing
        fields = '__all__'

class UpdateCinemaSerializer(serializers.ModelSerializer):
    """Обновление кинотеатра по идентификации"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'cinema_features',
            'phone',
            'location',
            'price',
            'social_networks',
            'amenities',
            'category',
            'health_and_safety_measures',
            'email',
        ]


class GetCinemaSerializer(serializers.ModelSerializer):
    """Вывод всех кинотеатров"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'cinema_features',
            'phone',
            'location',
            'price',
            'social_networks',
            'amenities',
            'category',
            'health_and_safety_measures',
            'email',
        ]
