from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Note

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