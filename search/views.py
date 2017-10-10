from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Url
import requests
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
    return render(request, 'search/index.html')

def result(request):
    url = request.GET.get('url')
    url2 = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=300'
    url3 = url
    html = requests.get(url3).text
    soup = BeautifulSoup(html)
    name = ''
    link = ''
    for member_tag in soup.select('.memberna_list dl dt a'):
        name += member_tag.text
        link += member_tag['href']
    context = {'url':url, 'name':name, 'link':link}

    return render(request, 'search/result.html', context)
