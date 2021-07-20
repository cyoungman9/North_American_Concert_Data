#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine


# In[2]:


csv_file = "../Homework/project_2/data/genre_totals.csv"
genre_total_df = pd.read_csv(csv_file)
genre_total_df.head()


# In[3]:


# Connect to local postgres database
from sqlalchemy import create_engine
rds_connection_string = "postgres:postgres@localhost:5432/Concerts"
engine = create_engine(f'postgresql://{rds_connection_string}')


# In[4]:


# Check for tables
engine.table_names()


# In[5]:


genre_total_df


# In[6]:


# Use pandas to load online csv converted DataFrame into database
genre_total_df.to_sql(name='genre_total', con=engine, if_exists='append', index=False)


# In[7]:


pd.read_sql_query('select * from genre_total', con=engine).head()


# In[8]:


csv_file = "../Homework/project_2/data/mtv_genres_final.csv"
mtv_genres_final_df = pd.read_csv(csv_file)
mtv_genres_final_df.head()


# In[9]:


mtv_genres_final_df.to_sql(name='mtv_genres_final', con=engine, if_exists='append', index=False)


# In[10]:


pd.read_sql_query('select * from mtv_genres_final', con=engine).head()


# In[11]:


csv_file = "../Homework/project_2/data/na_tour_final.csv"
na_tour_final_df = pd.read_csv(csv_file)
na_tour_final_df.head()


# In[12]:


#na_tour_final_df['gross_Mil'] = na_tour_final_df.gross_Mil.str.replace('$', ' ')

na_tour_final_df


# In[13]:


na_tour_final_df['avg_gross'] = na_tour_final_df.avg_gross.str.replace(',', '')
na_tour_final_df['avg_gross'] = na_tour_final_df.avg_gross.str.replace(' ', '')
na_tour_final_df['total_tick'] = na_tour_final_df.total_tick.str.replace(',', '')
na_tour_final_df['avg_tick'] = na_tour_final_df.avg_tick.str.replace(',', '')

na_tour_final_df


# In[14]:


na_tour_final_df.to_sql(name='na_tour_final', con=engine, if_exists='append', index=False)


# In[15]:


pd.read_sql_query('select * from na_tour_final', con=engine).head()


# In[16]:


csv_file = "../Homework/project_2/new_csv/concert_total.csv"
concert_total_df = pd.read_csv(csv_file)
concert_total_df.head()


# In[17]:


concert_total_df.to_sql(name='concert_total', con=engine, if_exists='append', index=False)


# In[18]:


pd.read_sql_query('select * from concert_total', con=engine).head()


# In[19]:


csv_file = "../Homework/project_2/data/tour_data_final.csv"
tour_data_final_df = pd.read_csv(csv_file)
tour_data_final_df.head()


# In[20]:


tour_data_final_df.to_sql(name='tour_data_final', con=engine, if_exists='append', index=False)


# In[21]:


pd.read_sql_query('select * from tour_data_final', con=engine).head()


# In[22]:


csv_file = "../Homework/project_2/new_csv/concert_count_both.csv"
concert_count_both = pd.read_csv(csv_file)
concert_count_both.head()


# In[23]:


concert_count_both.to_sql(name='concert_count_both', con=engine, if_exists='append', index=False)


# In[24]:


pd.read_sql_query('select * from concert_count_both', con=engine).head()


# In[25]:


csv_file = "../Homework/project_2/new_csv/concert_count_month.csv"
concert_count_month = pd.read_csv(csv_file)
concert_count_month.head()


# In[26]:


concert_count_month.to_sql(name='concert_count_month', con=engine, if_exists='append', index=False)


# In[27]:


pd.read_sql_query('select * from concert_count_month', con=engine).head()


# In[28]:


csv_file = "../Homework/project_2/new_csv/concert_count_year.csv"
concert_count_year = pd.read_csv(csv_file)
concert_count_year.head()


# In[29]:


concert_count_year.to_sql(name='concert_count_year', con=engine, if_exists='append', index=False)


# In[30]:


pd.read_sql_query('select * from concert_count_year', con=engine).head()


# In[31]:


year_df = pd.read_sql_query('select * from concert_count_year', con=engine).head()


# In[34]:


import plotly.express as px
import plotly

year_df = pd.read_sql_query('select * from concert_count_year', con=engine).head()
fig = px.bar(year_df, x="year", y="count", title="Number of Concerts by Year")

fig.show()
fig.write_html("fig_year.html")


# In[36]:


import json

fig_year = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

fig_year


# In[ ]:




