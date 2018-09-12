#coding = utf-8
import re
import os
from bs4 import BeautifulSoup
import requests
import urllib.request

url='http://www.win4000.com/sjzt/dilireba.html'

headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Mobile Safari/537.36'}

start_html = requests.get(url,headers=headers)

soup = BeautifulSoup(start_html.text,'lxml')
list = soup.find('div',class_='tab_box').find_all('a')
for li in list:
    title = li.get_text()
    href = li['href']
  #  a = 'href="http://www.win4000.com/mobile_detail_(.+?).html'
   # b = re.compile(href).findall(url)
    html=requests.get(href,headers=headers)
    html_soup = BeautifulSoup(html.text,'lxml')
    max_span = (html_soup.find('div',class_='ptitle').find_all('em')[0]).get_text()

    for page in range(1,int(max_span)+1):
        page_url = href[0:-5]+'_'+str(page)+'.html'
        img_html = requests.get(page_url,headers=headers)
        img_soup = BeautifulSoup(img_html.text,'lxml')
        img_url = img_soup.find('div',class_='main-wrap').find('img')['src']
        name = img_url[-17:-4]
        img = requests.get(img_url,headers=headers)
        print(img_url)
        # urllib.request.urlretrieve(img_url,filename='E:\\dilireba\\'+'%s.jpg'%name)




