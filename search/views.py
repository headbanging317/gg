# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Url
from requests import get
from bs4 import BeautifulSoup
import sys
import chardet
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.
def index(request):
    return render(request, 'search/index.html')

def result(request):
    url = request.get('url')
    url2 = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=300'
    url3 = url
    r = get(url)
    # html = requests.get(url3).text
    

    soup = BeautifulSoup(r.content.decode('euc-kr', 'replace'))
    
    
    name = ''
    link = ''
    for member_tag in soup.select('.memberna_list dl dt a'):
        name += member_tag.text
        link += member_tag['href']

    title = ''
    titles = soup.find_all('strong', id='articleBodyContents')
    
    for title_tag in soup.select('table tbody tr td p'):
        title += title_tag.text
    context = {'url':url, 'title':title}
 
    
    return render(request, 'search/result.html', context)

def get_text(request):
    url = request.GET.get('url')
    url2 = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=300'
    url3 = url
    html = requests.get(url3).text
    soup = BeautifulSoup(html)
    print(html)
    title = ''
    for item in soup.find_all('div', id='articleBodyContents'):
        title = title + str(item.find_all(text=True))
    context = {'url':url, 'title':title}
    return render(request, 'search/result.html', context)


