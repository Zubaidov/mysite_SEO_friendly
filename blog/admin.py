from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['created', 'author', 'publish', 'status']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}                          #autofill the slug from title
    raw_id_fields = ['author']                                          #while picking the post creator you will pick the user by it's ID, NOT BY NAME
    date_hierarchy = 'publish'                                          # hierarchy by the month and year
    ordering = ['status', 'publish']