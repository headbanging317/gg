# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Url
from requests import get
from bs4 import BeautifulSoup
import sys
import chardet
from .models import Full2
# Create your views here.
def index(request):
    return render(request, 'search/index.html')

def result(request):
    keyWord = request.GET.get('keyWord')
    page = int(request.GET.get('page'))
    full2 = Full2.objects.all()
    company = {}
    content = {}
    full = ['']
    dic = {'name':company, 'content':content}
  
    for i in range (1,page+1):
        s = str(i)
        url = 'http://www.saramin.co.kr/zf_user/search/recruit/page/'+s+'?pageCount=30&multiLine=&searchword='+ keyWord +'&company_cd=1&area=&domestic=&oversee=&jobCategory=&jobType=&career=&order=&periodType=&period=&condition=&arange=&company=&employ=&rSearchword=&hSearchword=&hInclude=&hExcept=&searchType=search&correctionSearch='
        r = get(url)
        # url2 = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=300'
        # url3 = url
        # html = requests.get(url3).text
        

        soup = BeautifulSoup(r.content.decode('utf-8', 'replace'))
        
        
        name = ''
        link = ''
        # for member_tag in soup.select('.memberna_list dl dt a'):
        #     name += member_tag.text
        #     link += member_tag['href']

        title = ''
        titles = soup.find_all('strong', id='articleBodyContents')


        companies = soup.select('.company_inbox li div div h2 a')
        contents = soup.select('.txt span a')

        

        for title_tag in companies:
            # company.append(title_tag.text)
            company[title_tag.text] = title_tag.get('href')
            

        # print (contents)
        for content_tag in contents:
            # content.append(content_tag.text)
            content[content_tag.text] = content_tag.get('href')
        # full = company + content
     
    
    context = {'url':url, 'company':company, 'content':content, 'keyWord':keyWord, 'full':full, 'dic':dic}
    
  
    return render(request, 'search/result.html', context)

# def get_text(request):
#     url = request.GET.get('url')
#     url2 = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=300'
#     url3 = url
#     html = requests.get(url3).text
#     soup = BeautifulSoup(html)
#     print(html)
#     title = ''
#     for item in soup.find_all('div', id='articleBodyContents'):
#         title = title + str(item.find_all(text=True))
#     context = {'url':url, 'title':title}
#     return render(request, 'search/result.html', context)


