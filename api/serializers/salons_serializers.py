from rest_framework import serializers

from api.models import Listing

class CreateSalonSerializer(serializers.ModelSerializer):
    """Добавление салона"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'salon_features',
            'phone',
            'location',
            'price',
            'social_networks',
            'amenities',
            'category',
            'health_and_safety_measures',
            'email',
        ]

class DeleteSalonSerializer(serializers.ModelSerializer):
    """Удаление салона по идентификации"""

    class Meta:
        model = Listing
        fields = '__all__'

class UpdateSalonSerializer(serializers.ModelSerializer):
    """Обновление салона по идентификации"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'salon_features',
            'phone',
            'location',
            'price',
            'social_networks',
            'amenities',
            'category',
            'health_and_safety_measures',
            'email',
        ]

class GetSalonSerializer(serializers.ModelSerializer):
    """Вывод всех салонов"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'salon_features',
            'phone',
            'location',
            'price',
            'social_networks',
            'amenities',
            'category',
            'health_and_safety_measures',
            'email',
        ]
