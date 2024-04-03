from rest_framework import serializers
from my_app.models import Books,Comment
from users.models import User
from django.contrib.auth import authenticate
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('name', 'description', 'pdf', 'photo', 'category', 'author','custom_user','country')

class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=50, write_only=True)
    username = serializers.CharField(max_length=255)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError({"Status": False, "message": "user not found"})
        return user

    def to_representation(self, user):
        refresh = RefreshToken.for_user(user)
        data = {
            "email": user.email,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data
    


class CommentSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source='books.name',)
    user_username = serializers.CharField(source='user.username', read_only=True)
    stars_given=serializers.CharField()
    class Meta:
        model = Comment
        fields = ['id', 'book_name', 'user_username', 'comment', 'stars_given',]
