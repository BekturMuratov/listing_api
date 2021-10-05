from rest_framework import generics
from api.models import Listing
from api.serializers import jobs_serializers


class CreateJobView(generics.CreateAPIView):
    """Добавление вакансии"""

    serializer_class = jobs_serializers.CreateJobSerializers


class DeleteJobByIdView(generics.DestroyAPIView):
    """Удаление вакансии по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = jobs_serializers.DeleteJobSerializer


class UpdateJobByIdView(generics.UpdateAPIView):
    """Обновление вакансии по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = jobs_serializers.UpdateJobSerializer


class GetJobView(generics.ListAPIView):
    """Вывод вакансии"""

    queryset = Listing.objects.filter(category=None)
    serializer_class = jobs_serializers.GetJobSerializer


class FindJobByIdView(generics.RetrieveAPIView):
    """Поиск вакансии по идентификации"""

    queryset = Listing.objects.all()
    serializer_class = jobs_serializers.GetJobSerializer
