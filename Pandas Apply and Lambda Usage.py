#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


d = {
        'nickname': ['bobg89', 'coolkid34','livelaughlove38'], 
        'state': ['NY', 'CA','TN'],
        'score': [100, 200,300]
    }
df = pd.DataFrame(data=d)
df_for_non_lambda = df.copy()
df_next_level = df.copy()


# In[3]:


df


# In[4]:


def add_some_love(state_value,score_value,name):
     if state_value == name:
          return score_value + 50
     else:
          return score_value


# In[5]:


df['love_added'] = df.apply(lambda x: add_some_love(x.state, x.score, 'NY'), axis=1)
df


# In[6]:


df_for_non_lambda


# In[7]:


#Big thanks to Étienne Célèry at https://stackoverflow.com/a/71608269/11736959
def add_some_love_non_lambda(row, name, add):
   if row.state == name:
       row.score = row.score + add
   return row


# In[8]:


df_for_non_lambda = df_for_non_lambda.apply(add_some_love_non_lambda, axis=1, args=('NY',40))
df_for_non_lambda


# In[9]:


def add_some_love_non_lambda_new(row, new_col, name, add):
   if row.state == name:
       row[new_col] = row.score + add
   else:
       row[new_col] = row.score  
   return row


# In[10]:


df_next_level = df_next_level.apply(add_some_love_non_lambda_new, axis=1, args=('love_added','NY',40))
df_next_level


# In[ ]:




