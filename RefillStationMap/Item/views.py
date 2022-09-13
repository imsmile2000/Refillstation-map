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
    # ui 상품 name 통일
    for i in items:
        # print(len(i.name))
        if len(i.name)>50:
            temp = i.name[:51]+"..."
            print(temp)
            name_board.append(temp)
        else:
            name_board.append(i.name)

    if request.method == "POST":

        filter1 = request.POST['filter1']
        filter2 = request.POST['filter2']
        filter3 = request.POST['filter3']
        
        #filter1
        price_low_filter = items.order_by('price')
        price_high_filter = items.order_by('-price')

        if filter1=="price_low":
            pagenator = Paginator(price_low_filter, 6)
            res_data["result_board"] = pagenator.get_page(page)
            return render(request,'item/products.html',res_data)
        if filter1=="price_high":
            pagenator = Paginator(price_high_filter, 6)
            res_data["result_board"] = pagenator.get_page(page)
            return render(request,'item/products.html',res_data)
        if filter1=="popular":
            pagenator = Paginator(price_low_filter, 6)
            res_data["result_board"] = pagenator.get_page(page)
            return render(request,'item/products.html',res_data)
        if filter1=="latest":
            pagenator = Paginator(price_low_filter, 6)
            res_data["result_board"] = pagenator.get_page(page)
            return render(request,'item/products.html',res_data)

        #filter2
        if filter1=="delivery_false":
            pagenator = Paginator(price_low_filter, 6)
            res_data["result_board"] = pagenator.get_page(page)
            return render(request,'item/products.html',res_data)
        if filter1=="delivery_true":
            pagenator = Paginator(price_low_filter, 6)
            res_data["result_board"] = pagenator.get_page(page)
            return render(request,'item/products.html',res_data)

        #filter3
        if filter3!="":
            pagenator = Paginator(price_low_filter, 6)
            res_data["result_board"] = pagenator.get_page(page)
            return render(request,'item/products.html',res_data)



    
        return render(request,'item/products.html',res_data)

        

    return render(request,'item/products.html',res_data)
