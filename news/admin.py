from django.contrib import admin
from .models import News, Category, Review

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    autocomplete_fields=['category','reporter']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields=['name']
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
