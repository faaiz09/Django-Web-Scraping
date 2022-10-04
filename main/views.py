from asyncio.base_subprocess import WriteSubprocessPipeProto
from email import contentmanager
import imp
from inspect import classify_class_attrs
from pkgutil import ImpImporter
from ssl import SSLSession
from tarfile import PAX_NAME_FIELDS
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def get_html_content(website):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session= requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'{website}').text
    return html_content

def home(request):
    site_data = None
    if 'website' in request.GET:
        #fetch website
        website = request.GET.get('website')
        html_content = get_html_content(website)
        soup = BeautifulSoup(html_content, 'html.parser')
        site_data = dict()
        site_data['Title']= soup.find('span',attrs={'class':'B_NuCI'}).text
        site_data['Url'] = print(website)
        site_data['Description'] = soup.find('div',attrs={'class':'_1AN87F'}).text
        site_data['Price'] = soup.find('div',attrs={'class':'_30jeq3 _16Jk6d'}).text
        #Image = soup.find('span',attrs={'class':'_2r_T1I _396QI4'}).img  
        
    return render(request,'main/home.html', {website : site_data})
