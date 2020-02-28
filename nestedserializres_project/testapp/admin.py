from django.contrib import admin
from testapp.models import Author,Book

class AuthorAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','subject')

class BookAdmin(admin.ModelAdmin):
    list_display=('id','title','author','release_date','rating')

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)    
