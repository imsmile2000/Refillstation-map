from django.shortcuts import redirect, render
from Item.item_save import item_save
from Item.models import Item
from django.core.paginator import Paginator
# Create your views here.

def save(request):

    item_save()
    return redirect(request,'/')

def item(request):

    res_data={}

    items = Item.objects.all()

    page = int(request.GET.get("p", 1))
    pagenator = Paginator(items, 6)
    res_data["result_board"] = pagenator.get_page(page)

    name_board=[]
    for i in items:
        # print(len(i.name))
        if len(i.name)>50:
            temp = i.name[:51]+"..."
            print(temp)
            name_board.append(temp)
        else:
            name_board.append(i.name)

    res_data['name_board'] = name_board


    return render(request,'item/products.html',res_data)
