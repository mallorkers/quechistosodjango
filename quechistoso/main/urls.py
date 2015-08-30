from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from api.viewsets import PublicationViewSet
from api.viewsets import ModerateViewSet
from api.viewsets import UserViewSet
from api import views
from apps.publications.views import PublicationList, PublicationDetail, PublicationForm, CreatePublication, \
    CategoriaList, LogoutView, NuevoUsuario

router = DefaultRouter()
router.register(r'publications', PublicationViewSet)
router.register(r'moderates', ModerateViewSet)
router.register(r'users', UserViewSet)



urlpatterns = patterns('',


    url(r'^$', PublicationList.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', PublicationDetail.as_view(), name='pub_detail'),
    url(r'^form/$', CreatePublication.as_view(), name='pub_form'),
    url(r'^categoria/(?P<slug>[-\w]+)/$', PublicationList.as_view(), name='categoria'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/publication/(?P<pk>[0-9]+)/$', views.PublicationDetail.as_view()),
    url(r'^api/', include(router.urls)),

    # login
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^salir/$', LogoutView.as_view(), name='salir'),
    url(r'^nuevo-usuario/$', NuevoUsuario.as_view(), name='nuevo-usuario'),
    )
