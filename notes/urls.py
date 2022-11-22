from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name="notes.detail"),
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
]

# urlpatterns = [
#     path('notes', views.get_all_list),
#     path('notes/<int:pk>', views.detail),
# ]
