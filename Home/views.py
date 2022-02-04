from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-01-03&sortBy=publishedAt&apiKey=3e7626aae282444b87411b2d86eaa99d'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    return render(request, 'index.html', {'articles': articles})