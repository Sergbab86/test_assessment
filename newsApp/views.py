from django.shortcuts import render
import requests
API_KEY = '624255a71d904827af047bd932b8faef'
# Create your views here.


def home(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()


    context = {
        'data': data
    }
    return render(request, 'newsApp/home.html', context)
