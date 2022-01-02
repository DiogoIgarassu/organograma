from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from setor.models import Setor
from .serializers import SetorSerializer

# Create your views here.
class SetorViewSet(ReadOnlyModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer