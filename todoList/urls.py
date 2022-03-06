from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('accounts/', include('django.contrib.auth.urls')),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("register", views.register, name="register"),
    path("tasks", views.tasks, name="tasks"),
    path("update_task", views.update_task, name="update_task"),
]

