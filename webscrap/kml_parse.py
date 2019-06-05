#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


# In[30]:


# url = "https://www.google.com/maps/d/kml?mid=1v_zuScFt4DMGO0BNGsmBmyiOyhU&forcekml=1" # all centers

# url = "https://www.google.com/maps/d/kml?mid=1GBr0_gE1VBUtJZRLJosLSl1B9Xo&forcekml=1" #snap 16<-14
# url = "https://www.google.com/maps/d/kml?mid=1hpyh201fVvv_p6oZKa6IOP8zzeebRy5p&forcekml=1" #casa 6<-6
# url = "https://www.google.com/maps/d/kml?mid=1GIYqt96Cbq-ppWyvVT0iJRLnbSk&forcekml=1" #hasa 13<-13
# url = "https://www.google.com/maps/d/kml?mid=1uC3LcicVmGp_CZcyQZkGuf8rLGY&forcekml=1" #job centers 30<-28
# url = "https://www.google.com/maps/d/kml?mid=1Ypu_qfcW7jBGDA_2uK1xP3TwUTw&forcekml=1" #medicaid offices 12<-12
# url = "https://data.cityofnewyork.us/api/views/fzk8-3ynb/rows.csv?accessType=DOWNLOAD" #medicaid offices open data
# url = "https://www.google.com/maps/d/kml?mid=1MYy3WOFBNgJ4D4-rqMYoXs2R3dk&forcekml=1" #ocss centers 10<-10

hra_centers = {"SNAP Centers": "https://www.google.com/maps/d/kml?mid=1GBr0_gE1VBUtJZRLJosLSl1B9Xo&forcekml=1",
       "CASA Offices": "https://www.google.com/maps/d/kml?mid=1hpyh201fVvv_p6oZKa6IOP8zzeebRy5p&forcekml=1",
       "HASA Centers": "https://www.google.com/maps/d/kml?mid=1GIYqt96Cbq-ppWyvVT0iJRLnbSk&forcekml=1",
       "Job Centers": "https://www.google.com/maps/d/kml?mid=1uC3LcicVmGp_CZcyQZkGuf8rLGY&forcekml=1",
       "Medicaid Offices": "https://www.google.com/maps/d/kml?mid=1Ypu_qfcW7jBGDA_2uK1xP3TwUTw&forcekml=1",
       "OCSS Centers": "https://www.google.com/maps/d/kml?mid=1MYy3WOFBNgJ4D4-rqMYoXs2R3dk&forcekml=1"
      }


# In[33]:


for center in hra_centers.keys():
  print(hra_centers[center])


# In[37]:


data = []
for center in hra_centers.keys():
    html_content = urllib.request.urlopen(hra_centers[center])
    soup = BeautifulSoup(html_content, 'html.parser')
    descriptions = soup.find_all('description')
    facility = soup.find_all('name')   
    for d in range(1,len(descriptions)):
        item = descriptions[d].text
        item = item.split('<br>')
    #     print(item)
        result = {}
        fclty = facility[d+1].text
        print(fclty)
        for i in range(len(item)):
            result['facility_name'] = fclty
            result['type'] = center
            parse = item[i].split(': ')
            key = parse[0]
            value = parse[1]
            result[key] = value
        data.append(result)
    # print(data)


# In[ ]:


# facility = soup.find_all('name')
# for i in range(2,len(facility)):
#     fclty = facility[i].text
#     print(fclty)


# In[38]:


len(data)


# In[39]:


pd.DataFrame(data)


# In[ ]:




