from django.urls import path, include
from . import views
from .views import addNotesView

urlpatterns = [
    path('', views.home, name = 'notes-home'),
    path('add_notes/', addNotesView.as_view(), name = 'notes-add'),
    path('notes/', views.notes, name = 'notes-content'),
]