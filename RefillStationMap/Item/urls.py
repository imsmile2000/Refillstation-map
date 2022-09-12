from django.urls import path,include
import Item.views as views

app_name = 'Item'

urlpatterns = [
    path('save',views.save,name='save'),
    path('',views.item,name='store'),

]