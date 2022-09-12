from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def about(request):
    
    return render(request,'about.html')

def store(request):

    return render(request,'store.html')

def components(request):

    return render(request,'app-components.html')