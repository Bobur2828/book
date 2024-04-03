from django.urls import path
from API.views import BookView,LoginApiView,CommentListCreateAPIView,CommentCRUD
app_name = 'api'
urlpatterns = [
    path('view_books/', BookView.as_view(), name='book_view'),
    path('view_books/<int:id>', BookView.as_view(), name='book_view'),
    path('login/', LoginApiView.as_view(), name='loginApiView'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentCRUD.as_view(), name='comment-detail'),


]