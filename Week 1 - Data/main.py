#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


file = pd.read_csv("books.csv")


# In[17]:


file


# In[28]:


count = 0
value = 0
n = len(file.Price)

for i in range(0,n):
    if file.loc[i,'Read'] == "Yes":
        count = count + 1
    value = value + file.loc[i,'Price']
    

    
print("You've read: ",(count/n)*100,"%")
print("Total Value: $",round(value,3))
print("Average Price: $",round(value/n,3))

