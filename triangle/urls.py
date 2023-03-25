from django.urls import path

from . import views

app_name = 'triangle'
urlpatterns = [
    path('triangle/', views.triangle, name='triangle'),
]
