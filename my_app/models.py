from django.db import models

class Books(models.Model):
    name=models.CharField(max_length=200, verbose_name='Kitob nomi')
    descrtiption=models.TextField(max_length=1000, verbose_name="Kitob haqida ma'lumot")

    pdf=models.FileField(upload_to='books/pdf', verbose_name="Kitob faylini yuklash")
    photo=models.ImageField(upload_to='books/photo', verbose_name="kitob rasmini kiriting")
    category = models.ForeignKey('Category', verbose_name='Kategoriyani tanlang', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', verbose_name='Muallifni tanlang', on_delete=models.CASCADE, blank=True, null=True)
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