from rest_framework import serializers

from api.models import Listing


class CreateJobSerializers(serializers.ModelSerializer):
    """Добавления вакансии """
    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'category',
            'image',
            'thumbnail',
            'vacancy_type',
            'qualification',
            'slug',
            'phone',
            'website',
            'social_networks'
            'location',
            'company',
            'salary',
            'amenities',
            'email',
        ]

class DeleteJobSerializer(serializers.ModelSerializer):
    """Удаление вакансии по идентификации"""

    class Meta:
        model = Listing
        fields = '__all__'

class UpdateJobSerializer(serializers.ModelSerializer):
    """Обновление вакансии по идентификации"""

    class Meta:
        model = Listing
        fields = '__all__'

class GetJobSerializer(serializers.ModelSerializer):
    """Вывод всех вакансии"""

    class Meta:
        model = Listing
        fields = [
            'id',
            'name',
            'description',
            'category',
            'image',
            'thumbnail',
            'vacancy_type',
            'qualification',
            'slug',
            'phone',
            'website',
            'social_networks'
            'location',
            'company',
            'salary',
            'amenities',
            'email',
        ]
