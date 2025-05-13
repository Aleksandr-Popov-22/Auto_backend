from Auto.models import Mark, Configuration, Model, Generation, Modification, Options, Specifications
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


class OptionsSerializer(serializers.ModelSerializer):


    class Meta:
        # Модель, которую мы сериализуем
        model = Options
        # Поля, которые мы сериализуем
        fields = '__all__'



class SpecificationsSerializer(serializers.ModelSerializer):


    class Meta:
        # Модель, которую мы сериализуем
        model = Specifications
        # Поля, которые мы сериализуем
        fields = '__all__'


class ModificationSerializer(serializers.ModelSerializer):

    options = OptionsSerializer(many=True, read_only=True)
    specifications = SpecificationsSerializer(many=True, read_only=True)


    class Meta:
        # Модель, которую мы сериализуем
        model = Modification
        # Поля, которые мы сериализуем
        fields = ['complectation_id', 'group_name', 'options', 'specifications']

class ConfigurationSerializer(serializers.ModelSerializer):

    modifications = ModificationSerializer(many=True, read_only=True)


    class Meta:
        # Модель, которую мы сериализуем
        model = Configuration
        # Поля, которые мы сериализуем
        fields = ['id', 'doors_count', 'body_type', 'configuration_name', 'modifications']



class ConfigurationCutSerializer(serializers.ModelSerializer):



    class Meta:
        # Модель, которую мы сериализуем
        model = Configuration
        # Поля, которые мы сериализуем
        fields = ['id', 'doors_count', 'body_type', 'configuration_name']





class GenerationSerializer(serializers.ModelSerializer):

    configurations = ConfigurationSerializer(many=True, read_only=True)
    



    class Meta:
        # Модель, которую мы сериализуем
        model = Generation
        # Поля, которые мы сериализуем
        fields = ['id', 'name', 'year_start', 'year_stop', 'is_restyle', 'model', 'configurations']


class GenerationCutSerializer(serializers.ModelSerializer):

    configurations = ConfigurationCutSerializer(many=True, read_only=True)
    



    class Meta:
        # Модель, которую мы сериализуем
        model = Generation
        # Поля, которые мы сериализуем
        fields = ['id', 'name', 'year_start', 'year_stop', 'is_restyle', 'model', 'configurations']











class GenerationCharacteristicSerializer(serializers.ModelSerializer):

    configurations = ConfigurationSerializer(many=True, read_only=True)


    class Meta:
        # Модель, которую мы сериализуем
        model = Generation
        # Поля, которые мы сериализуем
        fields = ['id', 'name', 'year_start', 'year_stop', 'is_restyle', 'model', 'configurations']



