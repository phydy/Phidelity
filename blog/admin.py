from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)

from django.contrib import admin
from .models import Post, Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'post', 'date_commented', 'active') 
    list_filter = ('active', 'date_commented') 
    search_fields = ('name', 'email', 'text') 
    actions = ['approve_comments'] 
    
    def approve_comments(self, request, queryset): 
        queryset.update(active=True)
