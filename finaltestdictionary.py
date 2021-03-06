# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:40:51 2019

@author: Harshini Priya
"""

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome(executable_path="G:\\chromedriver.exe", service_args=["--verbose", "--log-path=G:\\qc1.log"])
products=[] #List to store name of the product
prices=[] #List to store price of the product#List to store rating of the product
n=2
ratings=[]
x=int(input("enter 1:for laptops 2:for washing machine 3:for television and 4:for air conditioner"))
d={1:"https://www.flipkart.com/laptops/pr?sid=6bo,b5g&p[]=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree",2:"https://www.flipkart.com/home-kitchen/home-appliances/washing-machines/fully-automatic-front-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Fully%20Automatic%20Front%20Load",3:"https://www.flipkart.com/televisions/pr?sid=ckf,czl&p[]=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree",4:"https://www.flipkart.com/air-conditioners/pr?sid=j9e,abm,c54&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.technology%255B%255D%3DInverter&p[]=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree"}
url=d.get(x)
while n<6:
  driver.get(url)
  content = driver.page_source
  soup = BeautifulSoup(content,features="lxml")
  for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
     name=a.find('div', attrs={'class':'_3wU53n'})
     price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
     rating=a.find('div',attrs={'class':'hGSR34'})
     products.append(name.text)
     s=price.text
     tex=0
     try:
       ratings.append(rating.text)
       tex=rating.text
     except AttributeError:
         tex=0
         ratings.append('0')
     badch=["₹","$",","]
     for i in badch:
         s=s.replace(i,"")
     prices.append(str(s))
     print(name.text,price.text,tex)
  url_tag=soup.find('a',{'class':'_3fVaIS'})
  if n==2:
      url=url+"&page="+str(n)
  else:
      url=url[:-1]+str(n)
  n=n+1
df = pd.DataFrame({'Product Name':products,'Price':prices,'rating':ratings}) 
df.to_csv('finaltest.csv', index=True, encoding='utf-8')