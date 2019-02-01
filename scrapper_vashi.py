# -*- coding: utf-8 -*-
"""
Created on Sat May 19 18:35:17 2018

@author: Aditi
"""

from bs4 import BeautifulSoup as soup
import random
import requests
import re

agents = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
headers = {"User-Agent":random.choice(agents)}

url = "https://www.zomato.com/mumbai/vashi-restaurants"
response = requests.get(url,headers=headers)
print(response.text)
page_soup = soup(response.text, "html.parser")