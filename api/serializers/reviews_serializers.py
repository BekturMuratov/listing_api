from rest_framework import serializers

from api.models import Review

class CreateReviewSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = '__all__'

class DeleteReviewSerializer(serializers.ModelSerializer):
    """Удаление отзыва по идентификации"""

    class Meta:
        model = Review
        fields = '__all__'

class UpdateReviewSerializer(serializers.ModelSerializer):
    """Обновление отзыва по идентификации"""

    class Meta:
        model = Review
        fields = '__all__'

class GetReviewSerializer(serializers.ModelSerializer):
    """Вывод отзывов"""
    listing = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = [
            'email',
            'name',
            'text',
            'parent',
            'listing',
        ]
