from django.contrib import admin

# Register your models here.

from .models import Note

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    pass

admin.site.register(Note, NotesAdmin)
