from django.contrib import admin
from . import models
# Register your models here.

#admin.site.register(models.Post)
@admin.register(models.Post) #same as line 5
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created_on', 'publish', 'author')
    search_fields = ('title', 'article')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')