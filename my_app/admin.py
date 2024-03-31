from django.contrib import admin
from .models import Books,Category,Author,Slider, Ourteam

admin.site.register(Slider)

@admin.register(Ourteam)
class OurteamAdmin(admin.ModelAdmin):
    list_display = ('id', 'fi')

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','author','category','pdf')
    list_display_links = ('name','id')
    ordering = ('name',)

    list_per_page = 10
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name','id')
    ordering = ('name',)

    list_per_page = 10
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name','id')
    ordering = ('name',)

    list_per_page = 10



