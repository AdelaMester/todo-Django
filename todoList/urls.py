from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('accounts/', include('django.contrib.auth.urls')),
    path("request_identity/", views.request_identity, name="request_identity"),
]

