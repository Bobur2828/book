from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BooksSerializer,LoginSerializer,CommentSerializer
from my_app.models import Books,Comment
from rest_framework import generics, permissions
from rest_framework import generics
class LoginApiView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)

class BookView(APIView):
    permission_classes=(permissions.IsAuthenticated,)
    def get(self, request):
        books=Books.objects.all()
        serializer=BooksSerializer(books,many=True)      
        return Response(serializer.data)
    def post(self, request):
        serializer=BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request,id):
        book=Books.objects.get(id=id)
        serializer=BooksSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,id):
        book=Books.objects.get(id=id)
        book.delete()
        return Response({"message":"deleted succesfully"})
    

    
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

