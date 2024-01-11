from django.urls import path
from BookApp.views import *

urlpatterns = [
   path('',MainPageView.as_view(), name='main_page'),
   path('books_list/',BookListView.as_view(), name='books_list'),
   path('authors_list/',AuthorListView.as_view(), name='authors_list'),
   path('book_create/',BookCreateView.as_view(), name='book_create'),
   path('author_create/', AuthorCreateView.as_view(), name='author_create'),
   path('book_delete/<slug:slug>/',BookDeleleView.as_view(), name='book_delete'),
   path('author_delete/<int:pk>/',AuthorDeleteView.as_view(), name='author_delete'),
   path('book_detail/<slug:slug>/',BookDetailView.as_view(), name='book_detail'),
   path('author_detail/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
   path('book_update/<slug:slug>/',BookUpdateView.as_view(), name='book_update'),
   path('author_update/<int:pk>/',AuthorUpdateView.as_view(),name='author_update')

]
