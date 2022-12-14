from django.urls import path,include
import main.views as views

app_name = 'Home'

urlpatterns = [
    path('',views.index,name='main'),
    path('about',views.about,name='about'),
    path('wallet',views.wallet,name='wallet'),
    path('visit',views.visit,name='visit'),
    path('board',views.board,name='board'),
    path('store',views.store,name='store'),
    path('app-components',views.components,name='Map')

]