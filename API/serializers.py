from rest_framework import serializers
from my_app.models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('name', 'description', 'pdf', 'photo', 'category', 'author','custom_user','country')

