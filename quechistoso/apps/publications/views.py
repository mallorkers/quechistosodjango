# -*- encoding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, FormView, CreateView
from apps.publications.forms import PublicationForm
from apps.publications.models import Publication



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


class PublicationForm(FormView):
    template_name = 'publications/publication_form.html'
    form_class = PublicationForm
    success_url = '/thanks/'

    def form_valid(self, form):
        pass
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        # return super(ContactView, self).form_valid(form)


class CreatePublication(SuccessMessageMixin, CreateView):
    template_name = 'publications/publication_form.html'
    model = Publication
    fields = ('body', 'tags')
    success_url = '/'
    success_message = u'Registro creado correctamente'


    def form_valid(self, form):
        publication = form.save(commit=False)

        publication.status = 1

        publication.save()
        return super(CreatePublication, self).form_valid(form)


class CategoriaList(ListView):
    template_name = 'publications/index.html'
    context_object_name = 'publications'

    def get_queryset(self):
        queryset = Publication.objects.filter(tags__id=self.kwargs['pk']).filter(status=0)
        return queryset





class CreateUser(CreateView):
    pass
# def	 indice2(request):
#     ultimas_preguntas = Pregunta.objects.all().order_by('­fecha')[:5]
#     context = {'ultimas_preguntas': ultimas_preguntas }
#     return render(request, 'encuestas/index.html', context)
