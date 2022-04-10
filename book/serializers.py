from rest_framework import serializers
from book.models import Book
from author.models import Author
from author.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'count', 'authors',]
