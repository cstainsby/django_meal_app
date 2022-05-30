from django.shortcuts import render
from django.http import HttpResponse
from models import Recipe

# Create your views here.

# pass info into the html from inside the curly braces dictionary
# access in html using {{<var>.<operation>?}}
def index(request, id):
  return render(request, "meal_app/base.html", {})

def home(request):
  return render(request, "meal_app/home.html", {})