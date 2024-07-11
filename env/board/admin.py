from django.contrib import admin
from .models import Board, Post, Topic

# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_desc')
    def short_desc(self, obj):
        return obj.description[:10] + '...' if obj.description and len(obj.description) > 10 else obj.description

    short_desc.short_description = 'Desc'
    

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'last_updated')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('short_message', 'created_at','updated_at')
    def short_message(self,obj):
        return obj.message[:15] + '...' if obj.message and len(obj.message) > 15 else obj.message

    short_message.short_description = 'Msg'

    