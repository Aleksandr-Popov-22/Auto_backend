from django.http import HttpResponse

from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from Auto.serializers import MarkSerializer, ModelSerializer, GenerationSerializer, GenerationCutSerializer, GenerationCharacteristicSerializer
from Auto.models import Mark, Model, Generation, Configuration, Modification, Options, Specifications
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class MarkList(APIView):
    model_class = Mark
    serializer_class = MarkSerializer

    def get(self, request, format=None):

        marks = Mark.objects.all()

        if request.GET.get('search'):
            marks = Mark.objects.filter(name__icontains=request.GET.get('search'))       
        
        serializer = self.serializer_class(marks, many=True)    

        return Response(serializer.data)
    
class ModelList(APIView):
    model_class = Model
    serializer_class = ModelSerializer

    def get(self, request, id, format=None):

        models = self.model_class.objects.all().filter(mark=id)

        
        serializer = self.serializer_class(models, many=True)

    

        return Response(serializer.data)
    

class ModelDetail(APIView):
    model_class = Generation
    serializer_class = GenerationSerializer

    def get(self, request, id, id_model, format=None):


        generations = Generation.objects.all().prefetch_related('configurations').filter(model=id_model)


        serializer = GenerationCutSerializer(generations, many=True)

        return Response(serializer.data)
    

class ModelDetailCharacteristic(APIView):

    def get(self, request, id, id_model, format=None):

        '''generations = Generation.objects.all().prefetch_related(
            'configurations__modifications__options',
            'configurations__modifications__specifications'
        ).filter(model=id_model)'''
        generations = Generation.objects.all().filter(model=id_model)


        serializer = GenerationCharacteristicSerializer(generations, many=True)

        return Response(serializer.data)
