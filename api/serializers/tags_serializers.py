from rest_framework import serializers

from api.models import Tags

class CreateTagSerializer(serializers.ModelSerializer):
    """Добавление tag"""

    class Meta:
        model = Tags
        fields = '__all__'

class DeleteTagSerializer(serializers.ModelSerializer):
    """Удаление tag по идентификации"""

    class Meta:
        model = Tags
        fields = '__all__'

class UpdateTagSerializer(serializers.ModelSerializer):
    """Обновление tag по идентификации"""

    class Meta:
        model = Tags
        fields = '__all__'

class GetTagSerializer(serializers.ModelSerializer):
    """Вывод tag"""

    class Meta:
        model = Tags
        fields = '__all__'
