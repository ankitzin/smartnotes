from django.http import Http404
from django.shortcuts import render
from . import models
from .forms import NotesForm
from .models import Notes
from django.views.generic import ListView, DetailView, CreateView


class NotesCreateView(CreateView):
    success_url = '/smart/notes'
    form_class = NotesForm
    template_name = 'notes/notes_form.html'

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'


"""
Below are the function based view which is written in place of class view to learn properly
"""
# Create your views here.


def get_all_list(request):
    mynotes = models.Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes':mynotes})


def detail(request, pk):
    try:
        note = models.Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404(f"Notes Doesn't Exist error for id {pk}")
    return render(request, 'notes/notes_detail.html', {'note': note})
