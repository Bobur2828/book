from django.urls import path
from API.views import BookView
app_name = 'api'
urlpatterns = [
    path('view_books/', BookView.as_view(), name='book_view'),
]