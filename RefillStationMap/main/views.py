from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def about(request):
    
    return render(request,'about.html')

def store(request):

    return render(request,'store.html')

def wallet(request):

    return render(request,'wallet.html')

def visit(request):

    return render(request,'visit.html')

def board(request):

    return render(request,'board.html')

def components(request):

    return render(request,'app-components.html')
