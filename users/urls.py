from django.urls import path
from .views import user_login,user_register,user_logout, Yuklash,ProfileUpdateView,Profile

app_name = 'users'

urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('yuklash/', Yuklash, name='yuklash'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/', Profile.as_view(), name='profile'),





]