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
    
    # saramin list
    company_s = []
    content_s = []
    day_s = []
    detail_s = []

    # jobkorea list
    company_j = []
    content_j = []
    day_j = []
    detail_j = []

    full = ['']
    # dic = {'name':company, 'content':content}
  
    for i in range (1,page+1):
        s = str(i)
        url_s = 'http://www.saramin.co.kr/zf_user/search/recruit/page/'+s+'?pageCount=30&multiLine=&searchword='+ keyWord +'&company_cd=1&area=&domestic=&oversee=&jobCategory=&jobType=&career=&order=&periodType=&period=&condition=&arange=&company=&employ=&rSearchword=&hSearchword=&hInclude=&hExcept=&searchType=search&correctionSearch='
        saramin = get(url_s)
        url_j = 'http://www.jobkorea.co.kr/Search/?stext='+keyWord
        jobkorea = get(url_j)
        # url2 = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=300'
        # url3 = url
        # html = requests.get(url3).text
        

        soup_s = BeautifulSoup(saramin.content.decode('utf-8', 'replace'))
        soup_j = BeautifulSoup(jobkorea.content.decode('utf-8', 'replace'))
        
        name = ''
        link = ''
        # for member_tag in soup.select('.memberna_list dl dt a'):
        #     name += member_tag.text
        #     link += member_tag['href']

        title = ''
        # titles = soup.find_all('strong', id='articleBodyContents')

        # ---------- saramin scrapping---------- #
        companies_s = soup_s.select('.company_inbox li div div h2 a')
        contents_s = soup_s.select('.txt span a')
        days_s = soup_s.select('.txt .day')
        details_s = soup_s.select('.terms_li')

        for detail_tag in details_s:
            detail_s.append(detail_tag.text)

        for day_tag in days_s:
            day_s.append(day_tag.text)

        for title_tag in companies_s:
            company_s.append(title_tag.text)
            # company[title_tag.text] = title_tag.get('href')
            

        # print (contents)
        for content_tag in contents_s:
            content_s.append(content_tag.text)
            # content[content_tag.text] = content_tag.get('href')
        # full = company + content
     

        #---------- jobkorea scrapping----------#
        companies_j = soup_j.select('.corpName .giTitle')
        contents_j = soup_j.select('.gibInfo .devSpcfcGI')
        days_j = soup_j.select('#smGiList .devSpcfcGI .gibDay')
        details_j = soup_j.select('#smGiList .gibDesc .devSpcfcGI')

        for title_tag in companies_j:
            company_j.append(title_tag.text)

        for detail_tag in details_j:
            detail_j.append(detail_tag.text)

        for content_tag in contents_j:
            content_j.append(content_tag.text)

        for day_tag in days_j:
            day_j.append(day_tag.text)

        print('assd')
        print(company_j)
    context = {'url':url_s, 'company_s':company_s, 'content_s':content_s, 'keyWord':keyWord, 'full':full, 'day_s':day_s, 'detail_s':detail_s, 
                'company_j':company_j, 'content_j':content_j, 'detail_j':detail_j, 'day_j':day_j
    }
    
  
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


