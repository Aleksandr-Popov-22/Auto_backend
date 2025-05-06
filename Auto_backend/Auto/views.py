from django.http import HttpResponse

from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from Auto.serializers import MarkSerializer
from Auto.models import Mark, Model
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class MarkList(APIView):
    model_class = Mark
    serializer_class = MarkSerializer

    # Возвращает список акций
    def get(self, request, format=None):
        
        marks = self.model_class.objects.all()
        search = self.request.query_params.get('search')
        if search is not None:
            marks = marks.filter(name=search)
        
        serializer = self.serializer_class(marks, many=True)

    

        return Response(serializer.data)
    
class ModelList(APIView):
    model_class = Model
    serializer_class = MarkSerializer

    # Возвращает список акций
    def get(self, request, format=None):
        
        marks = self.model_class.objects.all()
        search = self.request.query_params.get('search')
        if search is not None:
            marks = marks.filter(name=search)
        
        serializer = self.serializer_class(marks, many=True)

    

        return Response(serializer.data)
    
