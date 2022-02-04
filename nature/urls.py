
from django.urls import path
from  . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blog',views.blog,name='blog'),
    path('post/<str:slug>',views.post,name='post'),
    path('about',views.about,name='about'),
    path('shop',views.shop,name='shop'),
    path('productview/<str:slug>',views.productview,name='productview'),
    path('services/fitness',views.fitness,name='fitness'),
    path('services/park',views.park,name='park'),
    # path('service',views.service,name='service'),
    path('search',views.search,name='search'),
    # path('water',views.water,name='water'),
    path('save_water',views.save_water,name='save_water')
   
  
     

]
