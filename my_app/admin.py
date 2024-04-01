from django.contrib import admin
from .models import Books,Category,Author,Slider, Ourteam,Comment,Reklama

admin.site.register([Slider,Reklama])

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

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment','books')




