# -*- coding: utf-8 -*-
"""
Created on Sat May 19 18:22:28 2018

@author: Aditi
"""

from bs4 import BeautifulSoup as soup
import random
import requests
import re
import numpy as np

agents = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
headers = {"User-Agent":random.choice(agents)}

url = "https://www.zomato.com/mumbai/vashi-restaurants"
response = requests.get(url,headers=headers)
print(response.text)
page_soup = soup(response.text, "html.parser")
top_users = page_soup.findAll("div",{"class":"top-user-rev-a"})
len(top_users)

filename = "experts_vashi.csv"
f = open(filename, "a+")
#headers = "Name, Level, Expertise, Followers Count, Restaurants Reviewed, Link\n"
#f.write(headers)

for top_user in top_users:
    
    name_raw = top_user.findAll("a")[1].text
    name = re.sub('[^A-Za-z0-9]+', '', name_raw)
    
    link = top_user.a["href"]
    
    count_raw = top_user.span.text
    count = re.sub('[^A-Za-z0-9]+', '', count_raw)
    
    
    agents = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
    headers = {"User-Agent":random.choice(agents)}    
    url = link
    response = requests.get(url,headers=headers)
    print(response.text)
    page_stat = soup(response.text, "html.parser")    
    stats = page_stat.findAll("div",{"class":"statistic"})
    
    level = stats[0].find("span",{"class","user-stats_rank"}).text
    #print(page_soup.findAll("div",{"class":"user-stats_rank"}))
    
    neighborhood = []
    if len(stats)!=1:       
        expertise = stats[1].findAll("li",{"class","badge"})
        for expert in expertise:
            neighborhood = np.append(neighborhood, expert.text.strip())
        str_neighborhood = "|".join(neighborhood)
    else: 
        neighborhood = "none"
    
    reviewed = []    
    res_names = page_stat.findAll("a",{"class","res_name"})
    for res_name in res_names:
        reviewed = np.append(reviewed, res_name.text )
    str_reviewed = "|".join(reviewed)    
    #print(reviewed)
    #print("Name: "+name+"  Count:"+count+" )
    f.write(name + "," + level + "," + str_neighborhood + "," + count + "," + str_reviewed + "," + link + "\n")
    
f.close()    