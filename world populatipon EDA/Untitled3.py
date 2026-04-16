#!/usr/bin/env python
# coding: utf-8

# In[ ]:


EDA         


# In[29]:


import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# In[30]:


df = pd.read_csv(r"C:\Users\lmodi\OneDrive\Documents\world_population.csv")
df


# In[31]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)
#pd.set_option('display.float_format', lambda x: '%.1f' % x)
#df = pd.DataFrame({"A":[1.2345, 2.6789]})

df


# In[32]:


df.info()


# In[34]:


df.describe()


# In[35]:


df.isnull().sum()


# In[36]:


df.nunique()


# In[37]:


df.sort_values(by='World Population Percentage', ascending=False).head()


# In[38]:


df.corr(numeric_only=True)


# In[39]:


sns.heatmap(df.corr(numeric_only=True),annot=True)

plt.rcParams['figure.figsize'] =(21,8)

plt.show()


# In[44]:


#df.groupby("Continent").mean()
numeric_cols = df.select_dtypes(include=['number']).columns
df.groupby("Continent")[numeric_cols].mean().sort_values(by="2022 Population",ascending=False)


# In[ ]:





# In[54]:


numeric_cols = df.select_dtypes(include=['number']).columns
df2 = df.groupby("Continent") [['1970 Population', '1980 Population', '1990 Population',
       '2000 Population', '2010 Population', '2015 Population',
       '2020 Population', '2022 Population']].mean().sort_values(by="2022 Population",ascending=False)
df2


# In[49]:


df.columns


# In[55]:


df3 = df2.transpose()
df3


# In[56]:


df3.plot()


# In[ ]:





# In[58]:


df.boxplot()


# In[ ]:





# In[60]:


df.select_dtypes(include="object")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




