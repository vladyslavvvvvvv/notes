from django.urls import path

from notes_app import views


urlpatterns = [
    path("", views.NoteListView.as_view(), name="note_list"),
    path("<int:pk>/", views.NoteDetailView.as_view(), name="note_detail"),
    
]
