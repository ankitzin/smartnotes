from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from . import models
from .forms import NotesForm
from .models import Notes
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    template_name = 'notes/notes_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()
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
