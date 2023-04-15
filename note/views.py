from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from note.forms import NoteForm

from .models import Note
LOGIN_URL ='/login'

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model=Note
    success_url="/smart/notes"
    template_name = "note/note_delete.html"
    login_url = LOGIN_URL

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model=Note
    form_class=NoteForm
    success_url="/smart/notes"
    login_url = LOGIN_URL

class NotesCreateView(LoginRequiredMixin, CreateView):
    model=Note
    form_class=NoteForm
    success_url="/smart/notes"
    login_url = LOGIN_URL

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        





class NotesListView(LoginRequiredMixin, ListView):
    model=Note
    context_object_name="notes"
    template_name="note/note_list.html"
    login_url = LOGIN_URL

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model=Note
    context_object_name="note"    
    template_name="note/note_detail.html"