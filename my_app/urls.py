from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('blog-left-sidebar/', views.blog_left_sidebar, name='blog_left_sidebar'),
    path('blog-no-sidebar/', views.blog_no_sidebar, name='blog_no_sidebar'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('error404/', views.error404, name='error404'),
    path('faq/', views.faq, name='faq'),
    path('index-2/', views.index_2, name='index_2'),
    path('index-box/', views.index_box, name='index_box'),
    path('my-account/', views.my_account, name='my_account'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-details/', views.portfolio_details, name='portfolio_details'),
    path('portfolio-three-column/', views.portfolio_three_column, name='portfolio_three_column'),
    path('shop-grid/', views.shop_grid, name='shop_grid'),
    path('shop-left-sidebar/', views.shop_left_sidebar, name='shop_left_sidebar'),
    path('shop-list/', views.shop_list, name='shop_list'),
    path('shop-no-sidebar/', views.shop_no_sidebar, name='shop_no_sidebar'),
    path('shop-right-sidebar/', views.shop_right_sidebar, name='shop_right_sidebar'),
    path('team/', views.team, name='team'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('search/', views.searchpage, name='searchpage'),
    path('detail/<int:id>/', views.BooksDetailView.as_view(), name='detail'),
    path('add_comment/<int:id>/', views.AddCommentView.as_view(),name='AddCommentView'),


]