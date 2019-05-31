#!/usr/bin/env python
# coding: utf-8

# In[102]:


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request


# In[143]:


# url = r"https://www.google.com/maps/d/kml?mid=1GBr0_gE1VBUtJZRLJosLSl1B9Xo&forcekml=1" #snap 16<-14
# url = r"https://www.google.com/maps/d/kml?mid=1hpyh201fVvv_p6oZKa6IOP8zzeebRy5p&forcekml=1" #casa 6<-6
# url = r"https://www.google.com/maps/d/kml?mid=1GIYqt96Cbq-ppWyvVT0iJRLnbSk&forcekml=1" #hasa 13<-13
# url = r"https://www.google.com/maps/d/kml?mid=1uC3LcicVmGp_CZcyQZkGuf8rLGY&forcekml=1" #job centers 30<-28
# url = r"https://www.google.com/maps/d/kml?mid=1MYy3WOFBNgJ4D4-rqMYoXs2R3dk&forcekml=1" #medicaid offices 10<-13
# url = "https://data.cityofnewyork.us/api/views/fzk8-3ynb/rows.csv?accessType=DOWNLOAD" #medicaid offices open data
# url = r"https://www.google.com/maps/d/kml?mid=1MYy3WOFBNgJ4D4-rqMYoXs2R3dk&forcekml=1" #ocss centers 10<-10
html_content = urllib.request.urlopen(url)
soup = BeautifulSoup(html_content, 'lxml-xml')


# In[146]:


# for description in descriptions:
#     html_soup = Soup(description.text, 'lxml') # Parse as HTML
# #     print(html_soup)
#     information = html_soup.find_all('p')
#     print(information)


# In[147]:


descriptions = soup.find_all('description')
type = descriptions[0].text
facility = soup.find_all('name')
data = []
for d in range(1,len(descriptions)):
    item = descriptions[d].text
    item = item.split('<br>')
#     print(item)
    result = {}
    for i in range(len(item)):
        fclty = facility[i+2].text
        result['facility_name'] = fclty
        result['type'] = type
        parse = item[i].split(': ')
        key = parse[0]
        value = parse[1]
        result[key] = value
    data.append(result)
print(data)


# In[148]:


# facility = soup.find_all('name')
# for i in range(2,len(facility)):
#     fclty = facility[i].text
#     print(fclty)


# In[149]:


len(data)


# In[ ]:




