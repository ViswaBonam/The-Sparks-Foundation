#!/usr/bin/env python
# coding: utf-8

# # GRIP by The Sparks Foundation
# 
# ## Data Science and Business Analytics Intern 
# 
# ### Task 3: Exploratory Data Analysis - Retail
# 
# ### Author: Bonam Viswa Sai Ammiraju
# 
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[2]:


url="https://docs.google.com/spreadsheets/d/e/2PACX-1vT0MRYSbOx5IqREcjgFP0lvmst-AMveg7hsbtKCyDP5ttKc6vdEpwKg6oSoXbcIQYqQrTVGEPH96ax7/pub?output=csv"
df_retail=pd.read_csv(url)


# In[3]:


df_retail.head()


# In[4]:


df_retail.tail()


# In[5]:


print('df_retail size:' ,df_retail.size)
print('df_retail shape:' ,df_retail.shape)


# In[6]:


df_retail.info()


# In[7]:


df_retail.describe()


# In[8]:


for colname,colval in df_retail.iteritems():
    print(colname,':',df_retail[colname].nunique())


# In[9]:


for colname,colval in df_retail.iteritems():
    if df_retail[colname].dtype==object:
        print(colname,':',df_retail[colname].unique())


# ## Univariate Analysis
# ### Categorial Data

# In[10]:


plt.figure(figsize=(10,5))
ax=sns.countplot(df_retail['Ship Mode'],palette='viridis')
plt.title('Most Sales by Shipping Mode')
ax.bar_label(ax.containers[0], label_type='edge');


# In[11]:


plt.figure(figsize=(10,5))
ax=sns.countplot(df_retail['Segment'],palette='magma')
plt.title('Customer Type by Segment')
ax.bar_label(ax.containers[0], label_type='edge');


# In[12]:


fig, ax = plt.subplots()
colors = ['darkslateblue', 'cornflowerblue', 'silver']
explode = (0.05, 0.05, 0.05, 0.05, 0.05)
ax.pie(df_retail['Segment'].value_counts(),labels=df_retail['Segment'].value_counts().index[0:],colors=colors,autopct='%.0f%%',pctdistance=0.85)
ax.set_title('Customer Type by Segment')
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle);


# In[13]:


plt.figure(figsize=(17,10))
ax=sns.countplot(y=df_retail['City'],order=df_retail['City'].value_counts().index[0:10],palette='plasma')
plt.title('Total Orders by Top 10 Cities')
ax.bar_label(ax.containers[0], label_type='edge');


# In[14]:


plt.figure(figsize=(17,10))
ax=sns.countplot(y=df_retail['State'],order=df_retail['State'].value_counts().index[0:10],palette='viridis')
plt.title('Total Orders for Top 10 State')
ax.bar_label(ax.containers[0], label_type='edge');


# In[15]:


plt.figure(figsize=(17,30))
ax=sns.countplot(y=df_retail['State'],order=df_retail['State'].value_counts().index[:])
plt.title('Total Orders for State')
ax.bar_label(ax.containers[0], label_type='edge');


# ### Category of products 

# In[16]:


plt.figure(figsize=(17,5))
ax=sns.countplot(df_retail['Category'],palette='plasma')
plt.title('Category')
ax.bar_label(ax.containers[0],label_type='edge');


# In[17]:


fig, ax = plt.subplots()
colors = ['darkslateblue', 'cornflowerblue', 'silver']
explode = (0.05, 0.05, 0.05, 0.05, 0.05)
ax.pie(df_retail['Category'].value_counts(),labels=df_retail['Category'].value_counts().index[0:],colors=colors,autopct='%.0f%%',pctdistance=0.85)
ax.set_title('Customer Type by Category')
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle);


# In[18]:


plt.figure(figsize=(17,5))
ax=sns.countplot(df_retail['Sub-Category'])
plt.title('Sub-Category')
ax.bar_label(ax.containers[0],label_type='edge');


# In[19]:


sns.boxplot(df_retail['Discount']);


# 
# ## Correlation

# In[20]:


df_retail.corr()


# In[21]:


sns.heatmap(df_retail.corr(),annot=True)
plt.rcParams['figure.figsize']=(17,5)


# ### Categories of products having same day ship mode

# In[22]:


df_retail[df_retail['Ship Mode']=='Same Day']['Category'].value_counts()


# In[23]:


plt.figure(figsize=(17,5))
ax=sns.barplot(x=df_retail[df_retail['Ship Mode']=='Same Day']['Category'].value_counts().index[0:3],y=df_retail[df_retail['Ship Mode']=='Same Day']['Category'].value_counts()[0:3],palette="hsv_r")
plt.xlabel('Categories',fontsize=12)
plt.ylabel('Product Counts',fontsize=12)
plt.title('No of Products and its categories having shipping mode same day',fontsize=15)
ax.bar_label(ax.containers[0],label_type='edge');


# ### Sub-categories of products having same day ship mode

# In[24]:


df_retail[df_retail['Ship Mode']=='Same Day']['Sub-Category'].value_counts()


# In[25]:


plt.figure(figsize=(17,5))
ax=sns.barplot(x=df_retail[df_retail['Ship Mode']=='Same Day']['Sub-Category'].value_counts().index[0:17],y=df_retail[df_retail['Ship Mode']=='Same Day']['Sub-Category'].value_counts()[0:17],palette="hsv_r")
plt.xlabel('Sub-Categories',fontsize=12)
plt.ylabel('Product Counts',fontsize=12)
plt.xticks(rotation=90)
plt.title('No of Products and its sub-categories having shipping mode same day',fontsize=15)
ax.bar_label(ax.containers[0],label_type='edge');


# ### Number of products having same day ship mode state-wise

# In[26]:


df_retail[df_retail['Ship Mode']=='Same Day']['State'].value_counts()


# In[27]:


plt.figure(figsize=(17,5))
ax=sns.barplot(x=df_retail[df_retail['Ship Mode']=='Same Day']['State'].value_counts().index[0:],y=df_retail[df_retail['Ship Mode']=='Same Day']['State'].value_counts()[0:],palette="hsv_r")
plt.xlabel('States',fontsize=12)
plt.ylabel('Product Counts',fontsize=12)
plt.xticks(rotation=90)
plt.title('No of Products per state having shipping mode same day',fontsize=15)
ax.bar_label(ax.containers[0],label_type='edge');


# ### Number of products having same day ship mode segment-wise

# In[28]:


df_retail[df_retail['Ship Mode']=='Same Day']['Segment'].value_counts()


# In[29]:


plt.figure(figsize=(17,5))
ax=sns.barplot(x=df_retail[df_retail['Ship Mode']=='Same Day']['Segment'].value_counts().index[0:],y=df_retail[df_retail['Ship Mode']=='Same Day']['Segment'].value_counts()[0:],palette="hsv_r")
plt.xlabel('Segment',fontsize=12)
plt.ylabel('Product Counts',fontsize=12)
plt.title('No of Products per segment having shipping mode same day',fontsize=15)
ax.bar_label(ax.containers[0],label_type='edge');


# ### Profits for products having same day ship mode

# In[30]:


sns.violinplot(df_retail[df_retail['Ship Mode']=='Same Day']['Profit'])
plt.title('Profits for products having same day ship mode',fontsize=15);


# In[31]:


plt.figure(figsize=(10,7))
plt.scatter(df_retail["Sales"] , df_retail["Profit"],color='r');


# ### Sales made by segment

# In[32]:


ax=sns.barplot(x='Segment', y='Sales', data=df_retail, palette='hsv_r')
plt.title('Most Sales by Segment')
ax.bar_label(ax.containers[0],label_type='edge');


# In[33]:


ax=sns.barplot(x='Quantity', y='Segment', data=df_retail, palette='hsv_r')
plt.title('Most Sales by Segment')
ax.bar_label(ax.containers[0],label_type='edge');


# ### Spread for Numerical Data

# In[34]:


df_retail.hist(bins=50 ,figsize=(20,15));


# # Summary
# 
# To conclude, if you are the Superstores owner who is planning to grow the store sales and get a better understanding on the customer behaviour to set up your own sales and marketing strategy, I suggest you should target *Consumer Segment* customer as they represented the most sales & quantity of items ordered across all segments. From a geographical point of view, you should target more on US West Region, for Cities, put more ads in *New York City*, *Los Angeles*, and *Philadelphia* while for States, put more marketing promotion in *California*, *New York* , and *Texas*.

# In[ ]:




