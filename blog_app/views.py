from django.shortcuts import render

# Create your views here.

def Index(request):
    context = {

    }
    
    return render(request, "blog_app/index.html",context)

def Menu(request):
    context = {

    }
    
    return render(request, "blog_app/menu/menu.html",context)