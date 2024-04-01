from .models import Category

def categorys(request):
    categorys=Category.objects.all()
    return {'categorys': categorys}

