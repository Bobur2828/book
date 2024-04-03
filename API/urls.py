from django.urls import path
from API.views import BookView,LoginApiView,CommentCRUD
app_name = 'api'
urlpatterns = [
    path('view_books/', BookView.as_view(), name='book_view'),
    path('view_books/<int:id>', BookView.as_view(), name='book_view'),
    path('login/', LoginApiView.as_view(), name='loginApiView'),
    path('comments/', CommentCRUD.as_view(), name='comment-list-create'),
    path('comments/<int:id>/', CommentCRUD.as_view(), name='comment-detail'),


]