# -*- coding: UTF-8 -*-
from serializers import PublicationsSerializer
from rest_framework import viewsets
from publications.models import Publication, UserProfile
from serializers import ModerateSerializer
from publications.models import Moderate
from api.serializers import UserProfileSerialzer

__author__ = 'ffernandez@apsl.net'


class PublicationViewSet(viewsets.ModelViewSet):

    serializer_class = PublicationsSerializer
    queryset = Publication.objects.all()


class ModerateViewSet(viewsets.ModelViewSet):

    serializer_class = ModerateSerializer
    queryset = Moderate.objects.all()

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserProfileSerialzer
    queryset = UserProfile.objects.all()


