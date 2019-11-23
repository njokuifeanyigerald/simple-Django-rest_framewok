from django.shortcuts import render
from .serializer import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer
from rest_framework import viewsets, permissions
from .models import Language, Paradigm,Programmer

# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer
class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

