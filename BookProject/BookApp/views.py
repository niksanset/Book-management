from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,DeleteView,UpdateView,CreateView
from BookApp.models import *
from django.urls import reverse,reverse_lazy


class MainPageView(TemplateView):
    template_name = 'BookApp/main_page.html'


class BookListView(ListView):
    template_name = 'BookApp/books_list_page.html'
    model = Book
    context_object_name = 'book_list'

class AuthorListView(ListView):
    template_name = 'BookApp/author_list_page.html'
    model = Author
    context_object_name = 'author_list'

class BookCreateView(CreateView):
    template_name = 'BookApp/add_book_page.html'
    model = Book
    fields = ('book_name','slug','author_book','year_publish','genre','rating',)
    success_url = reverse_lazy('books_list')

class AuthorCreateView(CreateView):
    template_name = 'BookApp/add_author_page.html'
    model = Author
    fields = ('__all__')
    success_url = reverse_lazy('authors_list')

class BookDeleleView(DeleteView):
    template_name = 'BookApp/book_delete_page.html'
    model = Book
    success_url = reverse_lazy('books_list')
class AuthorDeleteView(DeleteView):
    template_name = 'BookApp/author_delete_page.html'
    model = Author
    success_url = reverse_lazy('authors_list')

class BookDetailView(DetailView):
    template_name = 'BookApp/about_book_page.html'
    model = Book

class AuthorDetailView(DetailView):
    template_name = 'BookApp/about_author_page.html'
    model = Author
class BookUpdateView(UpdateView):
    template_name = 'BookApp/book_update_page.html'
    model = Book
    fields = ('__all__')
    success_url = reverse_lazy('books_list')

class AuthorUpdateView(UpdateView):
    template_name = 'BookApp/author_update_page.html'
    model = Author
    fields = ('__all__')
    success_url = reverse_lazy('authors_list')