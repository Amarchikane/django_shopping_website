from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
admin.site.site_header="Login in Devloper Amar"
admin.site.site_title="welcome to amar's dashboard"
admin.site.index_title="welcome to this portel "
urlpatterns = [
  path('home', views.home, name='home'),
  path('allproducts', views.allproducts, name='allproducts'),
  path('addproduct', views.addproduct, name='addproduct'),
  path('offer', views.offer, name='offer'),
  path('about', views.about, name='about'),
   path('cart', views.cart, name='cart'),
  path('delivery', views.delivery, name='delivery'),
  path('cantact', views.cantact, name='cantact'),
  path('login', views.login, name='login'),
  path('', views.main, name='main'),
  path('checkoutpage', views.checkoutpage, name='checkoutpage'),
   path('logout', views.logout, name='logout'),
   path('signup', views.signup, name='signup')
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)