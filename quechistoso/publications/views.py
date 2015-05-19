# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from publications.models import Publication


def indice(request):
    return render(request, 'publications/index.html')


class PublicationList(ListView):
    model = Publication
    template_name = 'publications/index.html'
    context_object_name = 'publications'
    paginate_by = 3
    queryset = Publication.objects.filter(status=0).order_by('-date_time')  # Filtramos las publicaciones en estado "publicado" -> 0

    def get_context_data(self):
        ctx = super(PublicationList, self).get_context_data()
        # ctx["tags"] = self.queryset.tags
        return ctx


class PublicationDetail(DetailView):

    model = Publication
    context_object_name = 'publication'



# def	 indice2(request):
#     ultimas_preguntas = Pregunta.objects.all().order_by('­fecha')[:5]
#     context = {'ultimas_preguntas': ultimas_preguntas }
#     return render(request, 'encuestas/index.html', context)
