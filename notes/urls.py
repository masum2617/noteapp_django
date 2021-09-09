from django.urls import path, include
from . import views
from .views import addNotesView, NotesUpdate, NotesDelete
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name = 'notes-home'),
    path('add_notes/', addNotesView.as_view(), name = 'notes-add'),
    path('note/<int:pk>/', NotesUpdate.as_view(), name = 'notes-update'),
    path('note/<int:pk>/delete', NotesDelete.as_view(), name = 'notes-delete'),
    path('notes/', views.notes, name = 'notes-content'),

    
] 