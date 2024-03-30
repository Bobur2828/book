from django.db import models

class Books(models.Model):
    name=models.CharField(max_length=200, verbose_name='Kitob nomi')
    descrtiption=models.TextField(max_length=1000, verbose_name="Kitob haqida ma'lumot")
    pdf=models.FileField(upload_to='books/pdf', verbose_name="Kitob faylini yuklash")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    