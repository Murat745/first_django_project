from django.urls import path

from . import views
from .views import person, update_person

app_name = 'triangle'
urlpatterns = [
    path('triangle/', views.triangle, name='triangle'),
    path('person', person, name='person'),
    path('person/<int:pk>', update_person, name='update_person'),
]
