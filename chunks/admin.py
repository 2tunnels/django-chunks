from django.contrib import admin
from defaults.admin import BaseTranslationAdmin

from .models import Chunk


class ChunkAdmin(BaseTranslationAdmin):
  list_display = ('key','description',)
  search_fields = ('key', 'content')

admin.site.register(Chunk, ChunkAdmin)
