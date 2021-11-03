from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import CourseSerializer
from .models import Course


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer