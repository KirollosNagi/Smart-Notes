from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=("title","text")
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control my-5"}),
            "text":forms.Textarea(attrs={"class":"form-control mb-5"}),
        }
        labels={
            "text": "Write your thoughts here"
        }

    