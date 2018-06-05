from django.contrib import admin
from blog.models import BlogArticle

# Register your models here.


class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ['title','author','publish',]
    list_display_links = ['publish',]
    list_filter =  ['title','author',]
    list_select_related = True
    list_per_page = 4
    list_editable = ['title',]
    search_fields = ['title',]


admin.site.register(BlogArticle,BlogArticleAdmin)