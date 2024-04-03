from django.shortcuts import render,get_object_or_404
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
    

                                                #CRUD faqat  royhatdan otgan user qoldirgan commentlarni  CRUD qila oladi holos     
class CommentCRUD(APIView):
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request):
        comment = Comment.objects.filter(user=request.user)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def put(self, request, id):
        comment = get_object_or_404(Comment, id=id, user=request.user)
        book=comment.books.name                         #put qilinganda  kitob nomini soramaslik uchun 
        request.data['user'] = request.user.id
        request.data['book_name']=book
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def post(self, request):
        a=request.data

        request.data['user'] = request.user.id
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, id):
        comment = Comment.objects.get(id=id)
        comment.delete()
        return Response({'status': True, 'message': 'Successfully deleted'})


