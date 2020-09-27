#!/usr/bin/env python
# coding: utf-8

# In[12]:


import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv


# In[13]:


#grabbing the webpage html
url = 'https://www.smh.com.au/topic/crime-5w4'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()


# In[17]:


#html parsing
page_soup = soup(page_html, "html.parser")

articles = page_soup.findAll("div", {"class":"X3yYQ undefined _31PXs"})
print(articles)


# In[15]:


article_title = []

for article in articles:
    title = article.find("a",{"data-test": "article-link"})
    article_title.append(title)

print(article_title)


# In[ ]:




