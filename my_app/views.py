from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, View
from .forms import AddCommentForm,CommentUpdateForm
from django.shortcuts import render
from .models import Slider,Books,Category, Ourteam,Comment
import requests
from django.contrib import messages
from django.http import HttpResponseForbidden
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
    teamm = Ourteam.objects.all()

    context = {
        'teamm': teamm
    }
    return render(request, 'my_app/about.html', context)


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

    book = Books.objects.all()

    context = {
        'book': book
    }
    
    return render(request, 'my_app/shop-grid.html', context)

def shop_left_sidebar(request):
    return render(request, 'my_app/shop-left-sidebar.html')

def shop_list(request):
    return render(request, 'my_app/shop-list.html')

def shop_no_sidebar(request):
    return render(request, 'my_app/shop-no-sidebar.html')

def shop_right_sidebar(request):
    return render(request, 'my_app/shop-right-sidebar.html')
def my_books(request):
    user=request.user
    user_books=Books.objects.filter(custom_user=request.user)
    comment=Comment.objects.filter(user=user).order_by('-created_at')
    user_comments = Comment.objects.filter(books__in=user_books)



    # books=Books.objects.filter(user=user
    return render(request, 'my_app/my_books.html',{'user_books':user_books,'comment':comment,'user_comments':user_comments})


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


class BooksDetailView(View):
    def get(self, request, id):
        form = AddCommentForm()
        books = get_object_or_404(Books, id=id)
        author = books.author
        author_books = Books.objects.filter(author=author)
        stars=Comment.objects.filter(books=books)
        star=stars.values('stars_given')
        
        stars_given_values = [item['stars_given'] for item in star]
        result = sum(stars_given_values)
        try:
            result1 = round(result / len(stars_given_values))
        except ZeroDivisionError:
            result1 = result
        
        print(result1)


        
        
        return render(request, 'my_app/single-product.html', {'form': form, 'books': books, 'author_books': author_books,'result1':result1})
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


def SendMsg(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    number = request.POST['number']
    message = request.POST['message']

    bot_token = '6437135033:AAHvK59HsWn_ZzDtCvNRfwARTkGQ8pRUTa0'
    text = 'Saytdan xabar: \n\nIsmi : ' + firstname + '\nFamilyasi : ' + lastname + '\nemail : ' + email + '\nTelefon nomer : ' + number + '\nXabar : ' + message
    url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='
    requests.get(url + '6516071223' + '&text=' + text)
    messages.success(request, (f"Xabaringiz muvaffaqiyatli yuborildi!!!"))

    return redirect('books:index',)


def Categorys(request, id):
    book = Books.objects.filter(category_id=id)
    category = Category.objects.all()

    context = {
        'book': book,
        'category': category,

    }
    return render(request, 'my_app/shop-grid.html', context)


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if comment.user == request.user:
        comment.delete()
        messages.success(request, "Xabar o'chirildi!")
        return redirect('books:detail', comment.books.id)
    
    messages.error(request, "Ushbu xabarga o'chirish huquqi yo'q")
    return redirect('books:detail', comment.books.id)



class CommentUpdate(View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.user == request.user:
            form = CommentUpdateForm(instance=comment)
            return render(request, 'my_app/comment_update.html', {'form': form, 'comment_id': comment_id})
        messages.success(request, "Sizda begona sharxni izohlash huquqingiz yoq")
        return redirect('books:detail', comment.books.id)

    
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.user == request.user:
            form = CommentUpdateForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('books:detail', comment.books.id)
            return render(request, 'my_app/comment_update.html', {'form': form, 'comment_id': comment_id})
        return HttpResponseForbidden("Sizga bu operatsiyani bajarishga ruxsat yo'q")
