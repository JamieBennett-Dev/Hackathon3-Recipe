from django.shortcuts import render, HttpResponse

recipes = [
    {
        'author': 'Chris',
        'title': 'Bangers & Mash',
        'instructions': 'lorem ipsum',
        'date_posted': 'June 24, 2024'
    },
    {
        'author': 'Brendan',
        'title': 'Chilli Con Carne',
        'instructions': 'lorem ipsum dorem',
        'date_posted': 'June 25, 2024'
    },
    {
        'author': 'Simon',
        'title': 'Chicken Tikka',
        'instructions': 'lorem ipsum dorem title',
        'date_posted': 'June 26, 2024'
    } 
]

# Create your views here.
def home(request):
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)
    

def about(request):
    return render(request, "recipes/about.html")



    