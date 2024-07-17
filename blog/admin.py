from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'status', 'created_on', 'updated_on')
    list_filter = ('author', 'status', 'created_on')
    search_fields = ('title', 'author__username', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)



