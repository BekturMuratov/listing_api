from rest_framework import generics
from api.models import Review
from api.serializers import reviews_serializers


class CreateReviewsViews(generics.CreateAPIView):
    """Добавления отзыва"""

    serializer_class = reviews_serializers.CreateReviewSerializer

class DeleteReviewViews(generics.DestroyAPIView):
    """ Удаления отзыва """

    queryset = Review.objects.all()

class UpdateReviewViews(generics.UpdateAPIView):
    """ Обновления отзыва """
    queryset = Review.objects.all()
    serializer_class = reviews_serializers.UpdateReviewSerializer


class GetReviewViews(generics.ListAPIView):
    """ВЫвод всех отзывов """

    queryset = Review.objects.all()
    serializer_class = reviews_serializers.GetReviewSerializer



