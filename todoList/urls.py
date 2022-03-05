from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

