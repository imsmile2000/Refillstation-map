from django.urls import path,include
import main.views as views

app_name = 'Home'

urlpatterns = [
    path('',views.index,name='main'),
    path('about',views.about,name='about'),
    path('store',views.store,name='store'),
    path('products',views.products,name='products'),
<<<<<<< HEAD
    path('app-components',views.components,name='Map')
=======
>>>>>>> 8258be236a64babd257eb4de277d4ffaafddfce9

]