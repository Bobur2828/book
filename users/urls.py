from django.urls import path
from .views import user_login,user_register,user_logout

app_name = 'users'

urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),




]