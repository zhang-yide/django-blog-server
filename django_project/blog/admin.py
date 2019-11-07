from django.contrib import admin

from blog.models import Category, Tag, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'modified_time', 'category', 'author')
    fields = ['title', 'body', 'excerpt', 'category', 'tags']
    ordering = ('-created_time',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
