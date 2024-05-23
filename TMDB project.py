#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
api_key="dab9f8901c9b7f7527340ec058b55ad6"
api_url="https://api.themoviedb.org/3"

params={'query': "game",'api_key':api_key}
header={'Accept':'application/json'}

response=requests.get(api_url + "/search/tv",headers=header,params=params)

data=response.json()
results=data.get('results')

# print(results)

for result in results:
    print(result['original_name'])


# In[11]:


# popular name search
   
import requests
api_key="dab9f8901c9b7f7527340ec058b55ad6"
api_url="https://api.themoviedb.org/3"

params={'query':"Jenna Ortega",'api_key':api_key}
header={'Accept':'application/json'}

response=requests.get(api_url + "/search/person",headers=header,params=params)

print(response.url)

data=response.json()
results=data.get('results')

for result in results:
   if(result['name']== 'Jenna Ortega'):
       print(result['original_name']+ " : " + str(result['id']))


# In[18]:


# Assume 'data' is a dictionary containing the 'results' key, which is a list.
results = data.get('results', [])

# Loop through each item in 'results'.
for result in results:
    # Fetch the 'known_for' list from the current result item.
    known_for = result.get('known_for', [])
    
    # Loop through each item in 'known_for'.
    for item in known_for:
        # Check if the 'original_name' of the item is "Wednesday".
        if item.get('original_name') == "Wednesday":
            # Print the 'overview' of the item.
            print(item.get('overview'))




# In[21]:


import requests
api_key="dab9f8901c9b7f7527340ec058b55ad6"
api_url="https://api.themoviedb.org/3"

# building our url
params={'with_cast':3894,'api_key':api_key,'sort_by':'popularity.desc'}
header={'Accept':'application/json'}

response=requests.get(api_url + "/discover/movie",headers=header,params=params)

print(response.url)

data=response.json()

results=data.get('results')

for result in results:
    print(result['title'] + ":" + str(result['popularity']))


# In[ ]:




