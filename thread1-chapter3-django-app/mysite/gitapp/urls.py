from django.urls import path

from . import views

app_name = 'gitapp'
urlpatterns = [
    path('', views.index, name='index'),
]
