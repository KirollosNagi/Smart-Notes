from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView


from note.forms import NoteForm

from .models import Note

class NotesDeleteView(DeleteView):
    model=Note
    success_url="/smart/notes"
    template_name = "note/note_delete.html"

class NotesUpdateView(UpdateView):
    model=Note
    form_class=NoteForm
    success_url="/smart/notes"

class NotesCreateView(CreateView):
    model=Note
    form_class=NoteForm
    success_url="/smart/notes"


class NotesListView(ListView):
    model=Note
    context_object_name="notes"
    template_name="note/note_list.html"

class NotesDetailView(DetailView):
    model=Note
    context_object_name="note"    
    template_name="note/note_detail.html"


    
# old way to display list view of object   
# def list(request):
#     all_notes=Note.objects.all()
#     return render(request,"note/note_list.html",{"notes":all_notes})


# old way to display detail view of object   
# def detail(request, pk):
#     detail=Note.objects.get(pk=pk)
#     return render(request,"note/note_detail.html",{"note":detail})