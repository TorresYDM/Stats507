# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
# 
# + [Topic dongming dongming@umich]
# For this question, please pick a topic - such as a function, class, method, recipe or idiom related to the pandas python library and create a short tutorial or overview of that topic. The only rules are below.
#     1. Pick a topic not covered in the class slides.
#     2. Do not knowingly pick the same topic as someone else.
#     3. Use bullet points and titles (level 2 headers) to create the equivalent of 3-5 “slides” of key points. They shouldn’t actually be slides, but please structure your key points in a manner similar to the class slides (viewed as a notebook).
#     4. Include executable example code in code cells to illustrate your topic.
# You do not need to clear your topic with me. If you want feedback on your topic choice, please discuss with me or a GSI in office hours.

# The function is DataFrame.pct_change()
# + [Topic Definition]
# This function always be used to calculate the percentage change between the current and a prior element, and always be used to a time series     
# The axis could choose the percentage change from row or columns
# Creating the time-series index 
ind = pd.date_range('01/01/2000', periods = 6, freq ='W') 
  
# Creating the dataframe  
df = pd.DataFrame({"A":[14, 4, 5, 4, 1, 55], 
                   "B":[5, 2, 54, 3, 2, 32],  
                   "C":[20, 20, 7, 21, 8, 5], 
                   "D":[14, 3, 6, 2, 6, 4]}, index = ind) 
  
# find the percentage change with the previous row 
df.pct_change()

# find the percentage change with precvious columns 
df.pct_change(axis=1)

# + [Topic Periods]
# periods means start to calculate the percentage change between the periods column or row and the beginning

# find the specific percentage change with first row
df.pct_change(periods=3)

# + [Topic fill_method]
# fill_method means the way to handle NAs before computing percentage change by assigning a value to that NAs
# importing pandas as pd 
import pandas as pd 
  
# Creating the time-series index 
ind = pd.date_range('01/01/2000', periods = 6, freq ='W') 
  
# Creating the dataframe  
df = pd.DataFrame({"A":[14, 4, 5, 4, 1, 55], 
                   "B":[5, 2, None, 3, 2, 32],  
                   "C":[20, 20, 7, 21, 8, None], 
                   "D":[14, None, 6, 2, 6, 4]}, index = ind) 
  
# apply the pct_change() method 
# we use the forward fill method to 
# fill the missing values in the dataframe 
df.pct_change(fill_method ='ffill')

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# + [Topic Title](#Topic-Title) 
# + [Topic 2 Title](#Topic-2-Title)

# ## Topic Title
# Include a title slide with a short title for your content.
# Write your name in *bold* on your title slide. 

