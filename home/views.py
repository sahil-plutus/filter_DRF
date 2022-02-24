from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter


class StudentApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    filter_fields = ['name']
    # ordering_fields = ['name']
    # search_fields = ['name']