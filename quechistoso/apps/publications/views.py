# -*- encoding: utf-8 -*-
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.core import urlresolvers

# Create your views here.
from django.views.generic import ListView, DetailView, FormView, CreateView, RedirectView
from apps.publications.forms import PublicationForm
from apps.publications.models import Publication, UserProfile, Tag


class PublicationList(ListView):
    model = Publication
    template_name = 'publications/home.html'
    context_object_name = 'publications'
    paginate_by = 3
    queryset = Publication.objects.filter(status=0).order_by(
        '-date_time')  # Filtramos las publicaciones en estado "publicado" -> 0

    def get_queryset(self):
        qs = super(PublicationList, self).get_queryset()
        category = self.kwargs.get('slug', '')
        if category:
            qs = qs.filter(tags__slug=category)
        return qs
    def get_context_data(self):
        ctx = super(PublicationList, self).get_context_data()
        ctx['tags'] = Tag.objects.all()
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
    template_name = 'publications/home.html'
    context_object_name = 'publications'

    def get_queryset(self):
        queryset = Publication.objects.filter(tags__slug=self.kwargs['slug']).filter(status=0)
        return queryset


class NuevoUsuario(RedirectView):
    permanent = False

    def dispatch(self, request, *args, **kwargs):
        UserProfile.objects.create(user=request.user)
        return super(NuevoUsuario, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwarest):
        return urlresolvers.reverse('home')


class LogoutView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return urlresolvers.reverse('home')
