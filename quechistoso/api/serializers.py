# -*- coding: UTF-8 -*-
from rest_framework import serializers
from publications.models import Publication, Moderate
from users.models import UserProfile
from publications.models import Comment

__author__ = 'ffernandez@apsl.net'



class ModerateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderate

class UserProfileSerialzer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','username')


class PublicationsSerializer(serializers.ModelSerializer):
    owner = UserProfileSerialzer()
    class Meta:
        model = Publication
        fields = ('id','status','body','session_id','tags','owner',)


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment


class PublicationDetailSerializer(serializers.ModelSerializer):
    owner = UserProfileSerialzer()
    #comments = CommentsSerializer()
    class Meta:
        model = Publication
        fields = ('id','status','body','session_id','tags','owner')


