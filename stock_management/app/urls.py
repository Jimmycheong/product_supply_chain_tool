from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_models', views.list_all_models),
    path('all_parts', views.list_all_parts)
]