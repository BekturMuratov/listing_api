from rest_framework import serializers

from api.models import Listing

class CreateRealEstateSerializer(serializers.ModelSerializer):
    """Добавление квартиры"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'phone',
            'location',
            'price',
            'social_networks',
            'amenities',
            'category',
            'health_and_safety_measures',
            'email'
        ]

class DeleteRealEstateSerializer(serializers.ModelSerializer):
    """Удаление квартиры по идентификации"""

    class Meta:
        model = Listing
        fields = '__all__'

class UpdateRealEstateSerializer(serializers.ModelSerializer):
    """Обновление квартиры по идентификации"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'phone',
            'location',
            'price',
            'social_networks',
            'amenities',
            'category',
            'health_and_safety_measures',
            'email',
        ]

class GetRealEstateSerializer(serializers.ModelSerializer):
    """Вывод всех квартир"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'phone',
            'location',
            'price',
            'social_networks',
            'amenities',
            'category',
            'health_and_safety_measures',
            'email',
        ]
