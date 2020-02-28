from django.shortcuts import render
from testapp.models import Author,Book
from testapp.serializers import AuthorSerializer,BookSerializer
from rest_framework import generics

class AuthorListView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class AuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
