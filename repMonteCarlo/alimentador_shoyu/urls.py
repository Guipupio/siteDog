from django.urls import path

from . import views

urlpatterns = [
    path('home_page', views.home_page, name='home_page'),
    path('sinal_alimentacao', views.trata_sinal_alimentacao, name='sinal_alimentacao'),
]