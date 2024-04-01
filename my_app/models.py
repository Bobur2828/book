from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User
from django.utils import timezone
class Books(models.Model):
    name=models.CharField(max_length=200, verbose_name='Kitob nomi')
    description=models.TextField(max_length=1000, verbose_name="Kitob haqida ma'lumot")

    pdf=models.FileField(upload_to='books/pdf', verbose_name="Kitob faylini yuklash")
    photo=models.ImageField(upload_to='books/photo', verbose_name="kitob rasmini kiriting")
    category = models.ForeignKey('Category', verbose_name='Kategoriyani tanlang', on_delete=models.CASCADE, related_name='books')
    author = models.ForeignKey('Author',verbose_name='Muallifni tanlang', on_delete=models.CASCADE, blank=True, null=True, related_name='author')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200, verbose_name='Kategoriya nomini kiriting')
    descrtiption=models.TextField(max_length=1000, verbose_name="Kategoriya haqida ma'lumot")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name=models.CharField(max_length=200, verbose_name='Muallif nomini kiriting')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Slider(models.Model):
    image=models.ImageField(upload_to='slider/image', verbose_name="slider rasmini kiriting")
    text1=models.CharField(max_length=200)

    def __str__(self):
        return self.text1

class Ourteam(models.Model):
    fi = models.CharField(max_length=80)  #Jamoa azolarini ismi familyasi
    photo = models.ImageField(upload_to='team/image', verbose_name="slider rasmini kiriting")
    occupation = models.CharField(max_length=70)
    twitter = models.CharField(max_length=110)
    facebook = models.CharField(max_length=170)
    linkedin = models.CharField(max_length=170)
    instagram = models.CharField(max_length=170)

    def __str__(self):
        return self.fi
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    stars_given = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user.username} commented to {self.books.name} and gave {self.stars_given} stars"
    
class Reklama(models.Model):
    text=models.CharField(max_length=250)
    image = models.ImageField(upload_to='reklama/image', verbose_name="Reklama")
    data_created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
    