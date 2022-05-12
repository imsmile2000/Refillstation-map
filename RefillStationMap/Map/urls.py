from django.urls import path,include
import Map.views as views

app_name = 'Map'

urlpatterns = [
    path('save',views.store,name='save'),
    path('',views.map,name='store'),

]