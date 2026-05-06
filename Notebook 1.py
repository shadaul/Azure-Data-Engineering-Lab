#!/usr/bin/env python
# coding: utf-8

# ## Notebook 1
# 
# 
# 

# In[1]:


get_ipython().run_cell_magic('pyspark', '', "df = spark.read.load('abfss://files@datalakeb9kljm3.dfs.core.windows.net/product_data/products.csv', format='csv'\n## If\u202fheader\u202fexists\u202funcomment\u202fline\u202fbelow\n, header=True\n)\ndisplay(df.limit(10))\n")


# In[2]:


df_counts = df.groupBy(df.Category).count()
display(df_counts)

