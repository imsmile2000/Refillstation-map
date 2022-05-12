from django.urls import path,include
import Map.views as views

app_name = 'Map'

urlpatterns = [
    path('',views.store,name='store'),

]