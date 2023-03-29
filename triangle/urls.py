from django.urls import path

from . import views


app_name = 'triangle'
urlpatterns = [
    path('triangle/', views.triangle, name='triangle'),
    path('person/', views.persons_all, name='persons_all'),
    path('person/create', views.create_person, name='create_person'),
    path('person/<int:pk>', views.update_person, name='update_person'),
]
