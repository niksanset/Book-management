from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=255, blank=True)
    author_last_name = models.CharField(max_length=255, blank=True)
    
    
   

    def __str__(self):
        return f"{self.author_name} - {self.author_last_name}"
    

class Genre(models.Model):
    genre_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.genre_name}"
    




class Book(models.Model):
    book_name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255,unique=True,blank=True)
    author_book = models.ForeignKey(Author, on_delete = models.CASCADE,blank=True)
    year_publish = models.PositiveIntegerField(blank=True)
    genre = models.ManyToManyField(Genre,blank=True)
    rating = models.PositiveIntegerField(default=0,blank=True)

    def __str__(self):
        return f"{self.book_name}"
