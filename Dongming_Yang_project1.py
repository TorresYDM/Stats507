#!/usr/bin/env python
# coding: utf-8

# # [Statistics 507, Fall 2021](https://jbhender.github.io/Stats507/F21/ps/index.html)
# **Problem Set 1**
# 
# **Student Name: Dongming Yang**
# 
# **StudentID:# 46323425**

# # Question 0 - Markdown warmup [10 points]
# ___
# This is question for [Problem set 1](https://jbhender.github.io/Stats507/F21/ps/ps1.html) of [Stats 507](https://jbhender.github.io/Stats507/F21/).
# 
# > Question 0 is about Markdown
# 
# The next question is about the **Fibonnaci sequence** $ F_n=F_{n-1}+F_{n-2} $. In part **a** we will define a Python functi
# on <code>fib_rec()</code>.
# 
# Below is a ...
# ### Level 3 Header
# Next, we can make a bulleted list:
# - Item 1
#   - detail 1
#   - detail 2
# - Item 2
# 
# Finally, we can make an enumerated list
# 
#     a.Item 1
#     b.Item 2
#     c.Item 3

# # Question1 - Fibonnaci Sequence [30]
# 1. Write a recursive function <code> fib_rec()</code> that takes a single input n and returns the value of $F_n$

# In[1]:


# Import package

import math
import time
import pandas as pd
import numpy as np
from scipy import stats

# Define the Function for rec 

def fib_rec(n):
    if n==1 or n==2:
        return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)
    
# Test the result of value of 7,11,13  

num_list=[7,11,13]
for n in num_list:
    print ('n=',n,' ','resutl=',fib_rec(n))


# In[2]:


# Calculate the time for fib_rec
# initial_run_number is the value that will compute first 
initial_run_number=30

# add_number will add to initial_value 
add_number=2

# The times for function perform for one number and get median
test_times=10

# The times for performance for different number 
total_run_times=5

fib_rec_list=[]
run_number=initial_run_number
for x in range (total_run_times):
    list=[]
    for y in range (test_times):
        start=time.process_time()
        fib_rec(run_number)
        end=time.process_time()
        list.append(end-start)
    run_number=run_number+add_number
    fib_rec_list.append('%.6f'% np.median(list))
    
# Print the result of time 

print (fib_rec_list)


# 2. Write a function <code>fib_for()</code> with the same signature that computes $F_n$ by summation using a for loop.

# In[3]:


# Define the function of fib_for 

def fib_for(n):
    a,b=0,1
    for i in range (n):
        a,b=b,a+b
    return a

# Test the result of value of 7,11,13  

num_list=[7,11,13]
for n in num_list:
    print ('n=',n,' ','resutl=',fib_for(n))


# In[4]:


# Calculate the time for fib_for

run_number=initial_run_number
fib_for_list=[]
for x in range (total_run_times):
    list=[]
    for y in range (test_times):
        start=time.process_time()
        fib_for(run_number)
        end=time.process_time()
        list.append(end-start)
    run_number=initial_run_number+add_number
    fib_for_list.append('%.6f'% np.median(list))
    
# Print the result     

print (fib_for_list)


# 3. Write a function <code>fib_whl()</code> with the same signature that computes $F_n$ by summation using a while loop.

# In[5]:


# Define the fucntion of fib_while

def fib_while(n):
    a,b=0,1
    index=1
    while index<n:
        a,b=b,a+b
        index=index+1
    return b

# Print the result of 7,11,13

num_list=[7,11,13]
for n in num_list:
    print ('n=',n,' ','resutl=',fib_while(n))


# In[6]:


# Calculate the time of fib_while 

run_number=initial_run_number
fib_while_list=[]
for x in range (total_run_times):
    list=[]
    for y in range (test_times):
        start=time.process_time()
        fib_while(run_number)
        end=time.process_time()
        list.append(end-start)
    run_number=run_number+add_number
    fib_while_list.append('%.6f'% np.median(list))
    
# Print the result     

print (fib_while_list)


# 4. Write a function <code>fib_rnd()</code> with the same signature that computes Fn using the rounding method described on the Wikipedia page linked above.

# In[7]:


# Define the function of fib_rnd

def fib_rnd(n):
    return round(((0.5*(1+5**0.5))**n)*(1/(5**0.5)))

# Print the result of 7,11,13

num_list=[7,11,13]
for n in num_list:
    print ('n=',n,' ','resutl=',fib_rnd(n))


# In[8]:


# Calculate the time of fib_rnd

run_number=initial_run_number
fib_rnd_list=[]
for x in range (total_run_times):
    list=[]
    for y in range (test_times):
        start=time.process_time()
        fib_rnd(run_number)
        end=time.process_time()
        list.append(end-start)
    run_number=run_number+add_number
    fib_rnd_list.append('%.6f'% np.median(list))
    
print (fib_rnd_list)


# 5. Write a function <code>fib_flr()</code> with the same signature that computes Fn using the truncation method described on the Wikipedia page linked above.

# In[9]:


# Define the function of fib_floor

def fib_flr(n):
    return math.ceil(((0.5*(1+5**0.5))**n)*(1/(5**0.5)))

# Print the result of 7,11,13

num_list=[7,11,13]
for n in num_list:
    print ('n=',n,' ','resutl=',fib_flr(n))


# In[10]:


# Calculate the time of fib_flr

run_number=initial_run_number
fib_flr_list=[]
for x in range (total_run_times):
    list=[]
    for y in range (test_times):
        start=time.process_time()
        fib_flr(run_number)
        end=time.process_time()
        list.append(end-start)
    run_number=run_number+add_number
    fib_flr_list.append('%.6f'% np.median(list))

print (fib_flr_list)


# 6. For a sequence of increasingly large values of n compare the median computation time of each of the functions above. Present your results in a nicely formatted table. (Point estimates are sufficient).

# In[11]:


# Combine all the time into map and transfer into matrix

map={'rec':fib_rec_list,'for':fib_for_list,'while':fib_while_list,"rnd":fib_rnd_list,"flr":fib_flr_list}
dp=pd.DataFrame(map)
list_run_number=[]
for i in range(total_run_times):
    list_run_number.append((initial_run_number+i*add_number))
dp.index=[('n='+str(x)) for x in list_run_number]
print(dp)


# # Question 2 - Pascal’s Triangle [20]
# 1. Write a function to compute a specified row of Pascal’s triangle.

# In[12]:


n=int(input("Enter the specified row number: "))
tri=[1,[1,1]]
for i in range(2,n):
    cur=[1]
    pre=tri[i-1]
    for x in range (i-1):
        cur.append(pre[x]+pre[x+1])
    cur.append(1)
    tri.append(cur)
print (cur)


# 2. Write a function for printing the first n rows of Pascal’s triangle using the conventional spacing with the numbers in each row staggered relative to adjacent rows. Use your function to display a minimum of 10 rows in your notebook.

# In[13]:


n=int(input("Enter the specified row number: "))
tri=[[1],[1,1]]

for i in range(2,n):
    cur=[1]
    pre=tri[i-1]
    for x in range (i-1):
        cur.append(pre[x]+pre[x+1])
    cur.append(1)
    tri.append(cur)
for x in range (n):
    line=''
    for y in range (x+1): 
        line=line+str(tri[x][y])+' '
    print(line.center(n*6))
    print('')


# # Question 3 - Statistics 101 [40]
# 1. The standard point and interval estimate for the populaiton mean based on Normal theory takes the form $x \pm z×se(x)$ where $ \overline{x} $ is the mean, $ se(x) $ is the standard error, and $z$ is a Gaussian multiplier that depends on the desired confidence level. Write a function to return a point and interval estimate for the mean based on these statistics.

# In[14]:



# Input confidential level 
level=float(input('Enter the confidential Level(In float ex:0.95):'))

# Input form
form_string='{0:.2f} [{1}% CI:({2:.3f},{3:.3f})]'

# Define the function to return est,lwr,upr,level
def None_dictionary(): 
    none_dic={'est','lwr','upr','level'}
    return none_dix


#Calculate the confidence interval
def method1(data,level,form_string): 
    
    try: 
        data=np.array(data)
    except: 
        print ('The data is not availble')
        
    est=data.mean()
    std=data.std(ddof=0)
    conf_interval = stats.norm.interval(level, loc=est, scale=std)
    lower=conf_interval[0]
    upper=conf_interval[1]
    try:
        string_output=form_string.format(est,level*100,lower,upper)
        return (string_output)
    except: 
        return None_dictionary()


# 2. There are a number of methods for computing a confidence interval for a population proportion arising from a Binomial experiment consisting of $n$ independent and identically distributed Bernoulli trials. Let $x$ be the number of successes in thes trials. In this question you will write a function to return point and interval estimates based on several of these methods. Your function should have a parameter method that controls the method used. Include functionality for each of the following methods.

# In[15]:



def method2(data,level,form_string):
    
    try: 
        data=np.array(data)
    except: 
        print ('The data is not availble')
        
    est=data.mean()
    z=stats.norm.ppf((1-level)/2+level,loc=0,scale=1)
    e=z*(est*(1-est)/n)**0.5
    upper=est+e
    lower=est-e
    string_output=form_string.format(est,level*100,lower,upper)
    
    try:
        string_output=form_string.format(est,level*100,lower,upper)
        return (string_output)
    except: 
        return None_dictionary()


# In[16]:


def method3(data,level,form_string):
    
    try: 
        data=np.array(data)
    except: 
        print ('The data is not availble')
        
    est=data.mean()
    upper=stats.beta.ppf(1-(1-level)/2,x+1,n-x)
    lower=stats.beta.ppf((1-level)/2,x,n-x+1)
    string_output=form_string.format(est,level*100,lower,upper)
    
    try:
        string_output=form_string.format(est,level*100,lower,upper)
        return (string_output)
    except: 
        return None_dictionary()


# In[17]:


def method4(data,level,form_string):
    
    try: 
        data=np.array(data)
    except: 
        print ('The data is not availble')
        
    est=data.mean()
    lower=max(0,stats.beta.ppf((1-level)/2,x+0.5,n-x+0.5))
    upper=min(stats.beta.ppf(1-(1-level)/2,x+0.5,n-x+0.5),1)
    string_output=form_string.format(est,level*100,lower,upper)
    
    try:
        string_output=form_string.format(est,level*100,lower,upper)
        return (string_output)
    except: 
        return None_dictionary()


# In[18]:


def method5(data,level,form_string):
    
    try: 
        data=np.array(data)
    except: 
        print ('The data is not availble')
        
    est=data.mean()
    z=stats.norm.ppf((1-level)/2+level,loc=0,scale=1)
    n_hat=n+z**2
    p_hat=(x+z**2/2)/n_hat
    e_hat=z*((1-p_hat)*p_hat/n_hat)**0.5
    upper=est+e_hat
    lower=est-e_hat
    string_output=form_string.format(est,level*100,lower,upper)
    
    try:
        string_output=form_string.format(est,level*100,lower,upper)
        return (string_output)
    except: 
        return None_dictionary()


# In[ ]:





# Create a 1d Numpy array with 42 ones and 48 zeros. Construct a nicely formatted table comparing 90, 95, and 99% confidence intervals using each of the methods above (including part a) on this data. Choose the number of decimals to display carefully to emphasize differences. For each confidence level, which method produces the interval with the smallest width?

# In[19]:


# Create the data list 
list=[]
n=90
x=42
for index in range (x):
    list.append(1)
for index in range (n-x):
    list.append(0)
    
# Transfer list into np.array into a data 
data=np.array(list)

level_list=[0.90,0.95,0.99]
list_map=[]
for level in level_list: 
    list_temp=[]
    list_temp.append(method1(data,level,form_string))
    list_temp.append(method2(data,level,form_string))
    list_temp.append(method3(data,level,form_string))
    list_temp.append(method4(data,level,form_string))
    list_temp.append(method5(data,level,form_string))
    list_map.append(list_temp)
df=pd.DataFrame(list_map)
df_transform=df.T
df_transform.index=['Normal Theory','Normal Approxinmation','Clopper-Pearon Interval',
            'Jeffreys Interval','Agresti-Coull Interval']
new_colmuns=['Level=90%','Level=95%','Level=99%']
df_transform.set_axis(new_colmuns,axis=1,inplace=True)
print (df_transform)

