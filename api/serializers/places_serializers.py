from rest_framework import serializers

from api.models import Listing

class CreatePlacesSerializer(serializers.ModelSerializer):
    """Добавление места отдыха"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'category',
            'amenities',
            'slug',
            'image',
            'thumbnail',
            'location',
            'phone',
            'social_networks',
            'price',
        ]

class DeletePlaceSerializer(serializers.ModelSerializer):
    """Удаление места отдыха по идентификации"""

    class Meta:
        model = Listing
        fields = '__all__'

class UpdatePlaceSerializer(serializers.ModelSerializer):
    """Обновление места отдыха по идентификации"""

    class Meta:
        model = Listing
        fields = '__all__'

class GetPlaceSerializer(serializers.ModelSerializer):
    """Вывод категорий"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'category',
            'amenities',
            'image',
            'thumbnail',
            'location',
            'phone',
            'social_networks',
            'price',
        ]
