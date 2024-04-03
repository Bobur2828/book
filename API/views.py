from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BooksSerializer
from my_app.models import Books
class BookView(APIView):
    def get(self, request):
        books=Books.objects.all()
        serializer=BooksSerializer(books,many=True)      
        return Response(serializer.data)
