from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def about(request):
    
    return render(request,'about.html')

def products(request):
    
    return render(request,'products.html')

def store(request):
    
<<<<<<< HEAD
    return render(request,'store.html')

def components(request):

    return render(request,'app-components.html')
=======
    return render(request,'store.html')
>>>>>>> 8258be236a64babd257eb4de277d4ffaafddfce9
