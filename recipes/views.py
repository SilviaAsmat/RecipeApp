from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the Recipes App</h1>")

def about(request):
    return HttpResponse("<h1>This is a recipes app to track recipes</h1>")