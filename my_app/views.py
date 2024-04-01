from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, View
from .forms import AddCommentForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider,Books,Category, Ourteam,Comment
def index(request):
    sliders=Slider.objects.all()
    books=Books.objects.all()
    search=request.GET.get('q','')
    if search:
        books=Books.objects.filter(name__icontains=search)
        data = {
        "sliders":sliders,
        "books":books,
    }

        
    else:
        data = {
        "sliders":sliders,
        "books":books,
    }
        



    

    return render(request, 'my_app/index.html', context=data)

def about(request):
    return render(request, 'my_app/about.html')


def blog(request):
    return render(request, 'my_app/blog.html')
def blog_details(request):
    return render(request, 'my_app/blog_details.html')

def blog_left_sidebar(request):
    return render(request, 'my_app/blog-left-sidebar.html')

def blog_no_sidebar(request):
    return render(request, 'my_app/blog-no-sidebar.html')

def cart(request):
    return render(request, 'my_app/cart.html')

def checkout(request):
    return render(request, 'my_app/checkout.html')

def contact(request):
    return render(request, 'my_app/contact.html')

def error404(request):
    return render(request, 'my_app/error404.html')

def faq(request):
    return render(request, 'my_app/faq.html')

def index_2(request):
    return render(request, 'my_app/index-2.html')

def index_box(request):
    return render(request, 'my_app/index-box.html')

def my_account(request):
    return render(request, 'my_app/my-account.html')

def portfolio(request):
    return render(request, 'my_app/portfolio.html')

def portfolio_details(request):
    return render(request, 'my_app/portfolio-details.html')

def portfolio_three_column(request):
    return render(request, 'my_app/portfolio-three-column.html')

def shop_grid(request):
    
    return render(request, 'my_app/shop-grid.html')

def shop_left_sidebar(request):
    return render(request, 'my_app/shop-left-sidebar.html')

def shop_list(request):
    return render(request, 'my_app/shop-list.html')

def shop_no_sidebar(request):
    return render(request, 'my_app/shop-no-sidebar.html')

def shop_right_sidebar(request):
    return render(request, 'my_app/shop-right-sidebar.html')



def team(request):

    teamm = Ourteam.objects.all()

    context = {
        'teamm' : teamm
    }

    return render(request, 'my_app/team.html', context)

def wishlist(request):
    return render(request, 'my_app/wishlist.html')

def test(request):
    return render(request, 'my_app/wishlist.html')


def searchpage(request):
    if 'qidiruv' in request.GET:
        qidiruv = request.GET['qidiruv']

        data = Books.objects.filter(name__icontains=qidiruv)
        print(data)
    else:
        data = Books.objects.all()
        print(data)
    context = {
        'data': data
    }
    return render(request, 'my_app/index.html', context)


# def single_product(request, id):
#     books=Books.objects.filter(id=id)
#     data={
#         "books":books
#     }
#     return render(request, 'my_app/single-product.html',context=data)

class BooksDetailView(View):
    def get(self, request, id):
        form=AddCommentForm()
        books=Books.objects.filter(id=id)
        return render(request, 'my_app/single-product.html',{'form':form,'books':books})

class AddCommentView(LoginRequiredMixin,View):
    def post(self, request,id):
        form=AddCommentForm(request.POST)
        books=Books.objects.filter(id=id)
        if form.is_valid():
            books=Books.objects.get(id=id)
            Comment.objects.create(
                user=request.user,
                books=books,
                comment=form.cleaned_data['comment'],
                stars_given=form.cleaned_data['stars_given'],
            )
            return redirect(reverse('books:detail', kwargs={'id':books.id}))
        return render(request, 'my_app/single-product.html',{'form':form,'books':books})