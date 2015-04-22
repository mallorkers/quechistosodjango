from rest_framework import generics
from publications.models import Publication
from serializers import PublicationDetailSerializer
from django.http import Http404
from requests import Response


class PublicationDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Publication.objects.all()
    #serializer_class = SnippetSerializer

    def get_object(self, pk):
        try:
            return Publication.objects.get(pk=pk)
        except Publication.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        publicacion = self.get_object(pk)
        serializer = PublicationDetailSerializer(publicacion)
        return Response(serializer.data)