from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "recipes/home.html")
    

def about(request):
    return render(request, "recipes/about.html")



    