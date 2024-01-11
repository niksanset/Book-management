from django.contrib import admin
from BookApp.models import *

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)