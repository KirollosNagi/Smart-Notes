from django.contrib import admin
from .models import Note

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Note, NotesAdmin)