from .models import Category, Books,Author,Reklama

def categorys(request):
    categorys=Category.objects.all()
    return {'categorys': categorys}

def related_books(request):
    related_books=Books.objects.all()
    return {'related_books':related_books}

def reklama(request):
    reklama=Reklama.objects.all()
    return {'reklama':reklama}