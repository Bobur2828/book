from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'my_app/index.html')

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

def single_product(request):
    return render(request, 'my_app/single-product.html')

def team(request):
    return render(request, 'my_app/team.html')

def wishlist(request):
    return render(request, 'my_app/wishlist.html')