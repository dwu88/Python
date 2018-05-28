
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


# In[16]:


r=requests.get("https://pythonhow.com/example.html")
c=r.content


# In[18]:


c


# In[21]:


soup=BeautifulSoup(c,"html.parser")


# In[39]:


all=soup.find_all('div',{'class':"cities"})


# In[43]:


all[0]


# In[52]:


all[0].find_all('p')[0].text


# In[56]:


for item in all:
    print(item.find_all("p")[0].text)

