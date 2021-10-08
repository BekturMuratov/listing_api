from rest_framework import serializers

from api.models import Listing

class CreateCarsSerializer(serializers.ModelSerializer):
    """Добавление автомобиля"""

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
            'technical_specifications',
            'category',
        ]

class DeleteCarsSerializer(serializers.ModelSerializer):
    """Удаление автомобиля по идентификации"""

    class Meta:
        model = Listing
        fields = '__all__'

class UpdateCarsSerializer(serializers.ModelSerializer):
    """Обновление автомобиля по идентификации"""

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
            'technical_specifications',
            'category',
        ]

class GetCarsSerializer(serializers.ModelSerializer):
    """Вывод всех автомобилей"""

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
            'technical_specifications',
            'category',
        ]
