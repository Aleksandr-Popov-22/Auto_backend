from Auto.models import Mark, Configuration, Model
#from Auto.models import AuthUser
from rest_framework import serializers


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Mark
        # Поля, которые мы сериализуем
        fields = ["id", "name", "country"]


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Model
        # Поля, которые мы сериализуем
        fields = ["id", "name"]


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Configuration
        # Поля, которые мы сериализуем
        fields = []
