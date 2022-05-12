from django.urls import path,include
import Map.views as views

app_name = 'Home'

urlpatterns = [
    path('',views.map,name='map'),

]