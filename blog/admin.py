from django.contrib import admin
from .models import Post, Comment, Newsletter

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'status', 'created_on')
  list_filter = ('status', )
  search_fields = ['title', 'content']
  prepopulated_fields = {'slug': ('title', )}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('name', 'body', 'post', 'created_on' )
  list_filter = ('created_on',)
  search_fields = ('name', 'body')

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
  list_display = ('email', 'entered_on', 'active')
  list_filter = ('email', 'entered_on', 'active')
  search_fields = ('email', )