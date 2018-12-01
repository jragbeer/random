import matplotlib.pyplot as plt
import os
from os import path
from wordcloud import WordCloud
import pyodbc
import datetime
import bs4 as bs
import numpy as np
import pandas as pd
from html.parser import HTMLParser

timee = datetime.datetime.now()
print(timee)
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=xxx;"
                      "Database=xxx;"
                      "Trusted_Connection=yes;")
# main table in database, has all of the text for the titles and descriptions
c = conn.cursor()
c.execute('SELECT Post_ID,Site_ID,Title,Description,Unique_Visits,All_Visits,Create_Date,Create_User_ID,Modified_Date,Modified_User_ID,Is_Active FROM dbo.Posts')
postsdf = pd.DataFrame([tuple(t) for t in c.fetchall()], columns = ['Post_ID','Site_ID','Title','Description','Unique_Visits','All_Visits','Create_Date','Create_User_ID','Modified_Date','Modified_User_ID','Is_Active'])
postsdf = postsdf[postsdf['Is_Active'] == True]
postsdf['Description'] = pd.Series([bs.BeautifulSoup(x, "lxml").get_text().replace('\n', ' ').replace('\r', ' ') for x in  postsdf['Description']], index = postsdf.index)

# table of all tag_ids, post_ids, but no text
c.execute('Select * from dbo.Post_Tags')
post_tagsdf = pd.DataFrame([tuple(t) for t in c.fetchall()],columns= ['Post_Tag_ID','Tag_ID','Post_ID','Unique_Visits','All_Visits','Is_Active'])
post_tagsdf = post_tagsdf[post_tagsdf['Is_Active'] == True]

# table of all tags, not linked with dbo.Posts
c.execute('Select * from dbo.Tags')
tagsdf = pd.DataFrame([tuple(t) for t in c.fetchall()],columns= ['Tag_ID','Keyword','Created_Date','Created_User_ID','Site_ID'])
newtagsdf = pd.merge(tagsdf, post_tagsdf, how = 'inner')
newtagsdf = newtagsdf[newtagsdf['Keyword'] != '']

#create list of tags for each unique post_id
uniquepostIDs = newtagsdf.Post_ID.unique()
tags_for_each_postID = pd.DataFrame(newtagsdf.groupby(['Post_ID'])['Keyword'].apply(list))

#merge the tags with the Posts df
newpostsdf = pd.merge(postsdf, tags_for_each_postID, how='left', left_on = 'Post_ID', right_index = True)
newpostsdf.set_index('Post_ID', inplace = True)
# print(newpostsdf)
# newpostsdf.to_csv('afdsdsZfds.csv')


# add a comment_count column to the Posts df
c.execute('Select * from dbo.Post_Comments')
postcommentsdf = pd.DataFrame([tuple(t) for t in c.fetchall()],columns= ['Post_Comment_ID','Comment_ID','Post_ID','Is_Active'])
postcommentsdf = postcommentsdf[postcommentsdf['Is_Active'] == True]
pcdf = pd.DataFrame(postcommentsdf.groupby(['Post_ID'])['Comment_ID'].count())
newpostsdf1 = pd.merge(newpostsdf, pcdf, how='left', left_index = True, right_index = True)
newpostsdf1.rename(columns={'Comment_ID': 'Comment_Count'}, inplace = True)
newpostsdf1['Comment_Count'].fillna(0, inplace = True)

c.execute('Select * from dbo.Events')
eventsdf = pd.DataFrame([tuple(t) for t in c.fetchall()],columns= ['Event_ID','Site_ID','Item_Type_ID','Event_Type_ID','Person_ID','Item_ID','Event_Date'])
eventsdf = eventsdf[eventsdf['Event_Type_ID'] == 4]
xxl = pd.DataFrame(eventsdf.groupby(['Item_ID'])['Event_ID'].count())
print(xxl)
newpostsdf0 = pd.merge(newpostsdf1, xxl, how='left', left_index = True, right_index = True)
newpostsdf0.rename(columns={'Event_ID': 'Like_Count'}, inplace = True)
newpostsdf0['Like_Count'].fillna(0, inplace = True)
newpostsdf0.to_csv('xxx.csv')
print(datetime.datetime.now()-timee)