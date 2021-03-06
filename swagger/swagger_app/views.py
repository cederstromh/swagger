# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.conf.urls import url
from django.http import HttpResponse

from swagger_app.models import Music
from swagger_app.serializers import MusicSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



# Create your views here
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    # permission_classes = (IsAuthenticated,)
