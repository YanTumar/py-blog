from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import Post, Commentary, User


# Вимога: unregister the Group model
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_time")
    list_filter = ("author", "created_time")
    search_fields = ("title", "content")
    date_hierarchy = "created_time"
    ordering = ("-created_time",)


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_time")
    list_filter = ("author", "created_time")
    search_fields = ("text",)
    date_hierarchy = "created_time"
    ordering = ("created_time",)
