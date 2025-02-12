#!/usr/bin/env python
# coding: utf-8

# # Project 
# 

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df_app=pd.read_csv(r"Application_data - application_data.csv")
df_app


# In[3]:


df_app.shape


# In[4]:


df_app.size


# In[5]:


df_app.index


# In[6]:


df_app.columns       


# In[7]:


df_app.columns.to_list()


# In[8]:


df_app.head()


# In[9]:


df_app.tail()


# In[10]:


df_app.info()


# In[11]:


df_app.info(verbose=True)


# In[12]:


df_app.info(verbose=True,show_counts=True)


# In[13]:


df_app.describe()


# In[14]:


df_app.describe().columns


# In[15]:


list(set(df_app.columns)-set(df_app.describe().columns))


# In[16]:


import pandas as pd
import numpy as np


# In[17]:


df_app["CODE_GENDER"]


# In[18]:


df_app.CODE_GENDER


# In[19]:


df_app[["CODE_GENDER","AMT_ANNUITY"]]


# In[20]:


#unique value count return karta hai (nunique)
# nunique() is a dataframe method that returns the unique value count of each column
df_app.nunique()


# In[21]:


df_app["CODE_GENDER"].unique()  # is a return of values


# In[22]:


#isnull() is a method of dataframe and it returns the n ull value in boolean..
#True -- if null exists.
df_app.isnull()


# In[23]:


#isna() -- predefined function of pandas for null values.
pd.isna(df_app)


# In[24]:


df_app.isnull().sum()


# In[25]:


df_app.isnull().mean()


# In[26]:


df_app.isnull().mean()*100


# In[27]:


round(df_app.isnull().mean()*100,2)


# In[28]:


#sort values is method used for sorting the records..
round(df_app.isnull().mean()*100,2).sort_values(ascending=False)


# In[29]:


def missing_value(Dataframe):
    return round(Dataframe.isnull().mean()*100,2).sort_values(ascending=False)


# In[30]:


missing_value(df_app)


# In[31]:


null=missing_value(df_app)[missing_value(df_app)>50]


# In[32]:


null


# In[33]:


null.index


# In[34]:


# drop() method 
# DataFrame.drop(columns,inplace)
df_app.drop(columns=null.index,inplace=True)
df_app


# In[35]:


null1=missing_value(df_app)[missing_value(df_app)>40]
null1


# In[36]:


null1.index


# In[37]:


df_app.drop(columns=null1.index,inplace=True)
df_app


# In[38]:


df_app["AMT_ANNUITY"].isnull().sum()


# In[39]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[40]:


sns.boxplot(df_app["AMT_ANNUITY"],color="green")
plt.show()


# In[41]:


df_app["AMT_ANNUITY"].describe()


# In[42]:


q1=np.quantile(df_app["AMT_ANNUITY"].dropna(),0.25)
q1


# In[43]:


q2=np.quantile(df_app["AMT_ANNUITY"].dropna(),0.50)
q2


# In[44]:


q3=np.quantile(df_app["AMT_ANNUITY"].dropna(),0.75)
q3


# In[45]:


IQR=q3-q1
IQR


# In[46]:


upper_fence=q3+1.5*(IQR)
lower_fence=q1-1.5*(IQR)


# In[47]:


l=[]
for i in df_app["AMT_ANNUITY"]:
     if i>upper_fence or i<lower_fence:
        l.append(i)
print(l)
   


# In[48]:


df_app["AMT_ANNUITY"]=df_app["AMT_ANNUITY"].fillna(df_app["AMT_ANNUITY"].median())


# In[49]:


df_app["AMT_ANNUITY"].isnull().sum()


# In[50]:


#kde= kurnel density estimator
#histogram plot
plt.figure(figsize=(8,6))
sns.histplot(df_app["AMT_ANNUITY"],kde=True,color="purple")
plt.show()


# In[51]:


df_app["AMT_GOODS_PRICE"].isnull().sum()


# In[52]:


df_app["AMT_GOODS_PRICE"].describe()


# In[53]:


sns.boxplot(df_app["AMT_GOODS_PRICE"],color="green")
plt.show()


# In[54]:


q1=np.quantile(df_app["AMT_GOODS_PRICE"].dropna(),0.25)
q1


# In[55]:


q2=np.quantile(df_app["AMT_GOODS_PRICE"].dropna(),0.50)
q2


# In[56]:


q3=np.quantile(df_app["AMT_GOODS_PRICE"].dropna(),0.75)
q3


# In[57]:


IQR=q3-q1
IQR


# In[58]:


upper_fence=q3+1.5*IQR
lower_fence=q1-1.5*IQR


# In[59]:


l=[]
for i in df_app["AMT_GOODS_PRICE"]:
     if i>upper_fence or i<lower_fence:
        l.append(i)
print(l)
   


# In[60]:


df_app["AMT_GOODS_PRICE"]=df_app["AMT_GOODS_PRICE"].fillna(df_app["AMT_GOODS_PRICE"]==df_app["AMT_CREDIT"])


# In[61]:


df_app["AMT_GOODS_PRICE"].isnull().sum()


# In[62]:


plt.figure(figsize=(8,6))
sns.histplot(df_app["AMT_GOODS_PRICE"],kde=True,color="black")
plt.show()


# In[63]:


df_app["OCCUPATION_TYPE"]


# In[64]:


df_app["OCCUPATION_TYPE"].isnull().sum()


# In[65]:


#value_counts()--records--frequency.
df_app["OCCUPATION_TYPE"].value_counts()


# In[66]:


df_app["OCCUPATION_TYPE"].value_counts(normalize=True)


# In[67]:


df_app["OCCUPATION_TYPE"]=df_app["OCCUPATION_TYPE"].fillna("Unknown")


# In[68]:


df_app["OCCUPATION_TYPE"].isnull().sum()


# In[69]:


occupation_type=df_app["OCCUPATION_TYPE"].value_counts()
occupation_type


# In[70]:


plt.figure(figsize=(12,8))
sns.barplot(x=occupation_type,y=occupation_type.index)
for index,value in enumerate(occupation_type):
    plt.text(value,index,f"{value}",ha="left",va="top",color="black",fontsize=12)
plt.show()


# In[71]:


df_app["NAME_TYPE_SUITE"]=df_app["NAME_TYPE_SUITE"].fillna("Unacompanied")


# In[72]:


df_app["NAME_TYPE_SUITE"].isnull().sum()


# In[73]:


X=df_app["NAME_TYPE_SUITE"].value_counts()
X


# In[74]:


plt.figure(figsize=(12,8))
sns.barplot(x=X,y=X.index)
for index,value in enumerate(X):
    plt.text(value,index,f"{value}",ha="left",va="center",color="black",fontsize=8)
plt.show()


# In[75]:


df_app["CNT_FAM_MEMBERS"]


# In[76]:


df_app["CNT_FAM_MEMBERS"].isnull().sum()


# In[77]:


df_app["CNT_FAM_MEMBERS"].describe()


# In[78]:


df_app["CNT_FAM_MEMBERS"]=df_app["CNT_FAM_MEMBERS"].fillna(df_app["CNT_FAM_MEMBERS"].median())


# In[79]:


df_app["CNT_FAM_MEMBERS"].isnull().sum()


# In[80]:


df_app.columns


# In[81]:


df_app[['AMT_REQ_CREDIT_BUREAU_HOUR', 'AMT_REQ_CREDIT_BUREAU_DAY',
       'AMT_REQ_CREDIT_BUREAU_WEEK', 'AMT_REQ_CREDIT_BUREAU_MON',
       'AMT_REQ_CREDIT_BUREAU_QRT', 'AMT_REQ_CREDIT_BUREAU_YEAR']]


# In[82]:


AMT_REQ_CREDIT=['AMT_REQ_CREDIT_BUREAU_HOUR', 'AMT_REQ_CREDIT_BUREAU_DAY',
       'AMT_REQ_CREDIT_BUREAU_WEEK', 'AMT_REQ_CREDIT_BUREAU_MON',
       'AMT_REQ_CREDIT_BUREAU_QRT', 'AMT_REQ_CREDIT_BUREAU_YEAR']


# In[83]:


df_app[AMT_REQ_CREDIT]


# In[84]:


df_app[AMT_REQ_CREDIT].isnull().sum()


# In[85]:


df_app[AMT_REQ_CREDIT].describe()


# In[86]:


plt.figure(figsize=(14,10))
sns.boxplot(df_app[AMT_REQ_CREDIT],color="seagreen")
plt.show()


# In[87]:


df_app[AMT_REQ_CREDIT]=df_app[AMT_REQ_CREDIT].fillna(df_app[AMT_REQ_CREDIT].median())


# In[88]:


df_app[AMT_REQ_CREDIT].isnull().sum()


# In[89]:


df_app.columns


# In[90]:


df_app[['OBS_30_CNT_SOCIAL_CIRCLE', 'DEF_30_CNT_SOCIAL_CIRCLE',
       'OBS_60_CNT_SOCIAL_CIRCLE', 'DEF_60_CNT_SOCIAL_CIRCLE']]


# In[91]:


SOCIAL_CIRCLE=['OBS_30_CNT_SOCIAL_CIRCLE', 'DEF_30_CNT_SOCIAL_CIRCLE',
       'OBS_60_CNT_SOCIAL_CIRCLE', 'DEF_60_CNT_SOCIAL_CIRCLE']
df_app[SOCIAL_CIRCLE]


# In[92]:


df_app[SOCIAL_CIRCLE].isnull().sum()


# In[93]:


df_app[SOCIAL_CIRCLE].describe()


# In[94]:


plt.figure(figsize=(14,10))
sns.boxplot(df_app[SOCIAL_CIRCLE],color="seagreen")
plt.show()


# In[95]:


df_app[SOCIAL_CIRCLE]=df_app[SOCIAL_CIRCLE].fillna(df_app[SOCIAL_CIRCLE].median())


# In[96]:


df_app[SOCIAL_CIRCLE].isnull().sum()


# In[97]:


plt.figure(figsize=(12,8))
sns.barplot(x=occupation_type,y=occupation_type.index)
for index,value in enumerate(occupation_type):
    plt.text(value,index,f"{value}",ha="left",va="top",color="black",fontsize=12)
plt.show()


# In[98]:


df_app["CODE_GENDER"]


# In[99]:


df_app["CODE_GENDER"].isnull().sum()


# In[100]:


df_app["CODE_GENDER"].value_counts()


# In[101]:


df_app["CODE_GENDER"].value_counts(normalize=True)


# In[102]:


df_app["CODE_GENDER"]=df_app["CODE_GENDER"].fillna("F")


# In[103]:


df_app["CODE_GENDER"].isnull().sum()


# In[104]:


code_gender=df_app["CODE_GENDER"].value_counts()
code_gender


# In[105]:


code_gender.index


# In[106]:


plt.figure(figsize=(16,8))
sns.barplot(x=code_gender,y=code_gender.index)
for index,value in enumerate(code_gender):
    plt.text(value,index,f"{value}",ha="left",va="center",color="black",fontsize=12)
plt.show()


# In[107]:


#loc -- loc is a labbeled based and meaning that we use labels(column_name,index_name to select aor exis data)
#loc(rows,columns]
# stop condition included
df_app.loc[0:10:2,["SK_ID_CURR","CODE_GENDER","AMT_ANNUITY","DAYS_BIRTH"]]


# In[108]:


#ILOC-- INTEGER BASED # NOT A INCLUDED STOP(N-1) 
df_app.iloc[0:10:2,0:10:2]


# In[109]:


df_app[df_app["AMT_ANNUITY"]>50000]


# In[110]:


df_app[df_app["CODE_GENDER"]=="F"]


# In[111]:


df_app[(df_app["AMT_ANNUITY"]>50000) & (df_app["CODE_GENDER"]=="F")]


# In[112]:


df_app.columns


# In[113]:


df_app[['DAYS_BIRTH','DAYS_EMPLOYED', 'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH','DAYS_LAST_PHONE_CHANGE']]


# In[114]:


#absolute fn== (-) change in (+)
df_app[['DAYS_BIRTH','DAYS_EMPLOYED', 'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH','DAYS_LAST_PHONE_CHANGE']]=abs(df_app[['DAYS_BIRTH','DAYS_EMPLOYED', 'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH','DAYS_LAST_PHONE_CHANGE']])
df_app[['DAYS_BIRTH','DAYS_EMPLOYED', 'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH','DAYS_LAST_PHONE_CHANGE']]




# In[115]:


df_app["DAYS_BIRTH_IN_YEAR"]=round(df_app["DAYS_BIRTH"]/365,2)
df_app["DAYS_BIRTH_IN_YEAR"]


# In[116]:


df_app["DAYS_EMPLOYED_IN_YEAR"]=round(df_app["DAYS_EMPLOYED"]/365,2)
df_app["DAYS_EMPLOYED_IN_YEAR"]
                                     


# In[117]:


df_app["DAYS_EMPLOYED_IN_YEAR"].max()


# In[118]:


df_app["DAYS_EMPLOYED_IN_YEAR"].describe()


# In[119]:


df_app["DAYS_EMPLOYED_IN_YEAR"]=df_app["DAYS_EMPLOYED_IN_YEAR"].replace(df_app["DAYS_EMPLOYED_IN_YEAR"].max(),np.nan)


# In[120]:


df_app["DAYS_EMPLOYED_IN_YEAR"].max()


# In[121]:


df_app["DAYS_BIRTH_RANGE"]=pd.cut(df_app["DAYS_EMPLOYED_IN_YEAR"],bins=[20,25,30,35,40,45,50,55,60,65,70],labels=["20-25","25-30","30-35","35-40","40-45","45-50","50-55","55-60","60-65","65&moore"])


# In[122]:


df_app["DAYS_BIRTH_RANGE"]


# In[123]:


df_app["DAYS_BIRTH_RANGE"].describe()


# In[124]:


df_app[["AMT_CREDIT","AMT_INCOME_TOTAL"]]


# In[125]:


df_app[["AMT_CREDIT_LAC","AMT_INCOME_TOTAL_LAC"]]=round(df_app[["AMT_CREDIT","AMT_INCOME_TOTAL"]]/100000,2)


# In[126]:


df_app[["AMT_CREDIT_LAC","AMT_INCOME_TOTAL_LAC"]]


# In[127]:


df_app[["AMT_CREDIT_LAC"]].describe()


# In[128]:


df_app["AMT_CREDIT_LAC_RANGE"]=pd.cut(df_app["AMT_CREDIT_LAC"],bins=[0,5,10,15,20,25,30,35,40,45],labels=["0-5l","5-10l","10-15l","15-20l","20-25l","25-30l","30-35l","35-40l","45&above"])


# In[129]:


df_app["AMT_CREDIT_LAC_RANGE"]


# In[130]:


df_app["AMT_CREDIT_LAC_RANGE"].value_counts()


# In[131]:


df_app["AMT_INCOME_TOTAL_LAC"].describe()


# In[132]:


df_app["AMT_INCOME_TOTAL_LAC_RANGE"]=pd.cut(df_app["AMT_INCOME_TOTAL_LAC"],bins=[0,1,2,3,4,5,6,7,8,9,10,100],labels=["0-1l","1-2l","2-3l","3-4l","4-5l","5-6l","6-7l","7-8l","8-9l","9-10l","100&above"])


# In[133]:


df_app["AMT_INCOME_TOTAL_LAC_RANGE"]


# In[134]:


df_app["AMT_INCOME_TOTAL_LAC_RANGE"].value_counts()


# In[135]:


df_pre=pd.read_csv(r"previous_application - previous_application.csv")
df_pre


# In[136]:


df_pre.head()


# In[137]:


df_pre.tail()


# In[138]:


df_pre.info()


# In[139]:


df_pre.describe()


# In[140]:


df_pre.shape


# In[141]:


df_pre.size


# In[142]:


df_pre.index


# In[143]:


df_pre.columns


# In[144]:


df_pre.columns.to_list()


# In[145]:


df_pre.describe().columns


# In[146]:


list(set(df_pre.columns)-set(df_pre.describe().columns))


# In[147]:


df_pre


# In[148]:


missing_value(df_pre)


# In[149]:


nullpre=missing_value(df_pre)[missing_value(df_pre)>50]


# In[150]:


nullpre.index


# In[151]:


df_pre.drop(columns=nullpre.index,inplace=True)


# In[152]:


df_pre


# In[153]:


df_pre["NAME_TYPE_SUITE"].isnull().sum()


# In[154]:


df_pre["NAME_TYPE_SUITE"]


# In[155]:


df_pre["NAME_TYPE_SUITE"]


# In[156]:


df_pre["NAME_TYPE_SUITE"]=df_pre["NAME_TYPE_SUITE"].fillna(df_pre["NAME_TYPE_SUITE"].mode()[0])


# In[157]:


df_pre["NAME_TYPE_SUITE"].isnull().sum()


# In[158]:


df_pre["AMT_GOODS_PRICE"]


# In[159]:


df_pre["AMT_GOODS_PRICE"].isnull().sum()


# In[160]:


sns.boxplot(df_pre["AMT_GOODS_PRICE"],color="green")
plt.show()


# In[161]:


df_pre["AMT_GOODS_PRICE"]=df_pre["AMT_GOODS_PRICE"].fillna(df_pre["AMT_GOODS_PRICE"]==df_pre["AMT_CREDIT"])


# In[162]:


df_pre["AMT_GOODS_PRICE"].isnull().sum()


# In[163]:


df_pre["AMT_ANNUITY"]


# In[164]:


df_pre["AMT_ANNUITY"].isnull().sum()


# In[165]:


sns.boxplot(df_pre["AMT_ANNUITY"],color="green")
plt.show()


# In[166]:


df_pre["AMT_ANNUITY"]=df_pre["AMT_ANNUITY"].fillna(df_pre["AMT_ANNUITY"].median())


# In[167]:


df_pre["AMT_ANNUITY"].isnull().sum()


# In[168]:


df_pre["PRODUCT_COMBINATION"]


# In[169]:


df_pre["PRODUCT_COMBINATION"].isnull().sum()


# In[170]:


df_pre["PRODUCT_COMBINATION"].value_counts()


# In[171]:


df_pre["PRODUCT_COMBINATION"]=df_pre["PRODUCT_COMBINATION"].fillna(df_pre["PRODUCT_COMBINATION"].mode()[0])


# In[172]:


df_pre["PRODUCT_COMBINATION"].isnull().sum()


# In[173]:


df_pre["CNT_PAYMENT"]


# In[174]:


df_pre["CNT_PAYMENT"].isnull().sum()


# In[175]:


sns.boxplot(df_pre["CNT_PAYMENT"],color="green")
plt.show()


# In[176]:


df_pre["CNT_PAYMENT"]=df_pre["CNT_PAYMENT"].fillna(df_pre["CNT_PAYMENT"].median())


# In[177]:


df_pre["CNT_PAYMENT"].isnull().sum()


# In[178]:


df_pre[["AMT_ANNUITY","AMT_CREDIT","AMT_APPLICATION"]]


# In[179]:


df_pre[["AMT_ANNUITY_LAC","AMT_CREDIT_LAC","AMT_APPLICATION_LAC"]]=round(df_pre[["AMT_ANNUITY","AMT_CREDIT","AMT_APPLICATION"]]/100000,2)


# In[180]:


df_pre[["AMT_ANNUITY_LAC","AMT_CREDIT_LAC","AMT_APPLICATION_LAC"]]


# In[181]:


list(set(df_pre.columns)-set(df_pre.describe().columns))


# In[182]:


df_pre.describe().columns


# In[183]:


df_pre[['DAYS_DECISION','DAYS_FIRST_DRAWING', 'DAYS_FIRST_DUE', 'DAYS_LAST_DUE_1ST_VERSION','DAYS_LAST_DUE', 'DAYS_TERMINATION']]


# In[184]:


df_pre[['DAYS_DECISION','DAYS_FIRST_DRAWING', 'DAYS_FIRST_DUE', 'DAYS_LAST_DUE_1ST_VERSION','DAYS_LAST_DUE', 'DAYS_TERMINATION']]=abs(df_pre[['DAYS_DECISION','DAYS_FIRST_DRAWING', 'DAYS_FIRST_DUE', 'DAYS_LAST_DUE_1ST_VERSION','DAYS_LAST_DUE', 'DAYS_TERMINATION']])


# In[185]:


df_pre[['DAYS_DECISION','DAYS_FIRST_DRAWING', 'DAYS_FIRST_DUE', 'DAYS_LAST_DUE_1ST_VERSION','DAYS_LAST_DUE', 'DAYS_TERMINATION']]


# In[186]:


df_pre[['DAYS_DECISION','DAYS_FIRST_DRAWING', 'DAYS_FIRST_DUE', 'DAYS_LAST_DUE_1ST_VERSION','DAYS_LAST_DUE', 'DAYS_TERMINATION']]=round(df_pre[['DAYS_DECISION','DAYS_FIRST_DRAWING', 'DAYS_FIRST_DUE', 'DAYS_LAST_DUE_1ST_VERSION','DAYS_LAST_DUE', 'DAYS_TERMINATION']]/365,2)


# In[187]:


df_pre[['DAYS_DECISION','DAYS_FIRST_DRAWING', 'DAYS_FIRST_DUE', 'DAYS_LAST_DUE_1ST_VERSION','DAYS_LAST_DUE', 'DAYS_TERMINATION']]


# In[188]:


df_pre["AMT_CREDIT_LAC"].value_counts()


# In[189]:


df_pre["AMT_CREDIT_LAC"].describe()


# In[190]:


df_pre["AMT_CREDIT_LAC_RANGE"]=pd.cut(df_pre["AMT_CREDIT_LAC"],bins=[0,5,10,15,20,25,30,35,40,45],labels=["0-5l","5-10l","10-15l","15-20l","20-25l","25-30l","30-35l","35-40l","40&more"])


# In[191]:


df_pre["AMT_CREDIT_LAC_RANGE"].value_counts()


# In[192]:


df_pre["AMT_ANNUITY_LAC"].value_counts()


# In[193]:


df_pre["AMT_ANNUITY_LAC"].describe()


# In[194]:


df_pre["AMT_APPLICATION_LAC"].value_counts()


# In[195]:


df_pre["AMT_APPLICATION_LAC"].describe()


# In[196]:


df_pre["AMT_APPLICATION_LAC_RANGE"]=pd.cut(df_pre["AMT_APPLICATION_LAC"],bins=[0,5,10,15,20,25,30,35,40],labels=["0-5l","5-10l","10-15l","15-20l","20-25l","25-30l","30-35l","35&more"])


# In[197]:


df_pre["AMT_APPLICATION_LAC_RANGE"].value_counts()


# In[198]:


df_app.groupby(["CODE_GENDER"])["AMT_ANNUITY"].mean()


# In[199]:


df_app.groupby(["CODE_GENDER","OCCUPATION_TYPE"])["TARGET"].count()


# In[200]:


df_app["TARGET"].value_counts()


# In[201]:


df_app.describe().columns.to_list()


# In[202]:


FLAG_COL=['FLAG_MOBIL','FLAG_EMP_PHONE','FLAG_WORK_PHONE','FLAG_CONT_MOBILE','FLAG_PHONE','FLAG_EMAIL']


# In[203]:


df_app[FLAG_COL]


# In[204]:


df_app["FLAG_MOBIL"]=df_app["FLAG_MOBIL"].apply(lambda x:"YES" if x==1 else "NO")


# In[205]:


df_app["FLAG_MOBIL"]


# In[206]:


df_app['FLAG_EMP_PHONE']=df_app['FLAG_EMP_PHONE'].apply(lambda x:"YES" if x==1 else "NO")


# In[207]:


df_app['FLAG_EMP_PHONE']


# In[208]:


df_app['FLAG_WORK_PHONE']=df_app['FLAG_WORK_PHONE'].apply(lambda x:"YES" if x==1 else "NO")


# In[209]:


df_app['FLAG_WORK_PHONE']


# In[210]:


df_app['FLAG_CONT_MOBILE']=df_app['FLAG_CONT_MOBILE'].apply(lambda x:"YES" if x==1 else "NO")


# In[211]:


df_app['FLAG_CONT_MOBILE']


# In[212]:


df_app['FLAG_PHONE']=df_app['FLAG_PHONE'].apply(lambda x:"YES" if x==1 else "NO")


# In[213]:


df_app['FLAG_PHONE']


# In[214]:


df_app['FLAG_EMAIL']=df_app['FLAG_EMAIL'].apply(lambda x:"YES" if x==1 else "NO")


# In[215]:


df_app['FLAG_EMAIL']


# In[216]:


df_app["CREDIT_RATIO"]=round(df_app["AMT_CREDIT"]/df_app["AMT_INCOME_TOTAL"],2)


# In[217]:


df_app["CREDIT_RATIO"]


# In[218]:


#numerical analysis
df_app.describe().columns


# In[219]:


numerical_columns=['AMT_ANNUITY', 'DAYS_BIRTH_IN_YEAR', 'DAYS_EMPLOYED_IN_YEAR','AMT_CREDIT_LAC','AMT_INCOME_TOTAL_LAC','CREDIT_RATIO','CNT_FAM_MEMBERS']


# In[220]:


numerical_columns


# In[221]:


def uni_numerical_analysis(dataframe,columns):
    sns.set(style="darkgrid")
    plt.figure(figsize=(25,10))

    plt.subplot(1,3,1)
    sns.boxplot(data=dataframe,x=columns,orient="v").set(title="boxplot")

    plt.subplot(1,3,2)
    sns.histplot(dataframe[columns],kde=True).set(title="hisplot")

    plt.show()
    


# In[222]:


import warnings
warnings.filterwarnings("ignore")


# In[223]:


for i in numerical_columns:
    uni_numerical_analysis(df_app,i)
    


# In[224]:


list(set(df_app.columns)-set(df_app.describe().columns))


# In[225]:


categorical_columns=['OCCUPATION_TYPE',
 'AMT_GOODS_PRICE',
 'NAME_EDUCATION_TYPE',
 'NAME_INCOME_TYPE',
 'FLAG_OWN_CAR',
 'NAME_HOUSING_TYPE',
 'FLAG_WORK_PHONE',
 'AMT_INCOME_TOTAL_LAC_RANGE',
 'FLAG_MOBIL',
 'DAYS_BIRTH_RANGE',
 'CODE_GENDER',
 'NAME_TYPE_SUITE',
 'NAME_FAMILY_STATUS',
 'FLAG_EMAIL',
 'FLAG_OWN_REALTY',
 'FLAG_PHONE',
 'FLAG_EMP_PHONE',
 'FLAG_CONT_MOBILE',
 'ORGANIZATION_TYPE',
 'NAME_CONTRACT_TYPE',
 'AMT_CREDIT_LAC_RANGE',
 'WEEKDAY_APPR_PROCESS_START']


# In[226]:


def uni_categorical_analysis(dataframe,columns):
    sns.set(style="darkgrid")
    plt.figure(figsize=(15,8))

    sns.barplot(x=dataframe[columns].value_counts(),y=dataframe[columns].value_counts().index)
    for index,value in enumerate(dataframe[columns].value_counts()):
        plt.text(value,index,f" {value}",ha="left",va="center",color="black",fontsize=10)
    plt.show()


# In[227]:


for i in categorical_columns:
    uni_categorical_analysis(df_app,i)
    


# In[228]:


df_pre.describe().columns


# In[229]:


list(set(df_pre.columns)-set(df_pre.describe().columns))


# In[230]:


#target analysis


# In[231]:


Target_variable_payment_difficulty=df_app[df_app["TARGET"]==1]
Target_variable_payment_others=df_app[df_app["TARGET"]==0]


# In[232]:


Target_variable_payment_difficulty


# In[233]:


Target_variable_payment_others


# In[234]:


df_app.describe().columns


# In[235]:


numerical_data_1=['AMT_ANNUITY','AMT_GOODS_PRICE','DAYS_BIRTH_IN_YEAR', 'DAYS_EMPLOYED_IN_YEAR', 'AMT_CREDIT_LAC','AMT_INCOME_TOTAL_LAC', 'CREDIT_RATIO','CNT_FAM_MEMBERS']


# In[236]:


numerical_data_1


# In[237]:


list(set(df_app.columns)-set(df_app.describe().columns))


# In[249]:


categorical_data_1=['FLAG_OWN_CAR','NAME_HOUSING_TYPE', 'NAME_FAMILY_STATUS','AMT_INCOME_TOTAL_LAC_RANGE','DAYS_BIRTH_RANGE','CODE_GENDER','NAME_INCOME_TYPE','NAME_CONTRACT_TYPE','FLAG_OWN_REALTY','NAME_EDUCATION_TYPE','NAME_TYPE_SUITE','DAYS_BIRTH_RANGE']


# In[250]:


categorical_data_1


# In[251]:


def target_categorical_uni(dataframe, variable, dataframe_difficulty, dataframe_others):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(25, 8))
    
    # Plot for payment difficulty
    sns.countplot(
        x=variable,
        data=dataframe_difficulty,
        linewidth=1,
        ax=ax1,
        edgecolor="black",
        hue=variable,
        palette=sns.color_palette("dark", n_colors=dataframe_difficulty[variable].nunique())
    )
    ax1.set_ylabel("Total Count")
    ax1.set_title(f"Distribution of {variable} in Payment Difficulty", fontsize=18)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=40, ha="right")
    
    for p in ax1.patches:
        ax1.annotate(
            f"{(p.get_height() / len(dataframe_difficulty) * 100):.1f}%",
            (p.get_x() + p.get_width() / 2, p.get_height() + 5),
            ha="center",
            weight="bold"
        )
    
    # Plot for other payments
    sns.countplot(
        x=variable,
        data=dataframe_others,
        linewidth=1,
        ax=ax2,
        edgecolor="black",
        hue=variable,
        palette=sns.color_palette("dark", n_colors=dataframe_others[variable].nunique())
    )
    ax2.set_ylabel("Total Count")
    ax2.set_title(f"Distribution of {variable} in Other Payments", fontsize=18)
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=40, ha="right")
    
    plt.tight_layout()
plt.show()


# In[252]:


target_categorical_uni(df_app,"CODE_GENDER",Target_variable_payment_difficulty,Target_variable_payment_others)


# In[ ]:





# In[253]:


for i in categorical_data_1:
    target_categorical_uni(df_app,i,Target_variable_payment_difficulty,Target_variable_payment_others)
    


# In[254]:


def target_numerical_uni(variable):
    sns.set(style="darkgrid")
    plt.figure(figsize=(15,8))


    plt.subplot(1,2,1)
    sns.histplot(Target_variable_payment_difficulty[variable],kde=True)
    plt.title(f'distribution of {variable} in payment difficulty',fontsize=15)
    plt.xlabel("variable")


    plt.subplot(1,2,2)
    sns.histplot(Target_variable_payment_others[variable],kde=True)
    plt.title(f'distribution of {variable} in payment difficulty',fontsize=15)
    plt.xlabel("variable")
plt.show()



# In[255]:


target_numerical_uni("CREDIT_RATIO")


# In[256]:


for i in numerical_data_1:
    target_numerical_uni(i)


# In[257]:


#bi-variate analysis
sns.scatterplot(x=Target_variable_payment_difficulty["AMT_ANNUITY"],y=Target_variable_payment_difficulty["AMT_GOODS_PRICE"],data=Target_variable_payment_difficulty,hue="TARGET")
plt.show()


# In[258]:


#pie chart

color=sns.color_palette("bright")
plt.pie(x=df_app["CODE_GENDER"].value_counts(),labels=df_app["CODE_GENDER"].value_counts().index,colors=color,autopct="%.1f%%")
plt.title("CODE-GENDER")
plt.show()


# In[259]:


df_app.columns


# In[260]:


df_app.groupby(['CODE_GENDER'])['TARGET'].mean()*100


# In[261]:


df_app.groupby(['AMT_ANNUITY'])['TARGET'].mean()*100


# In[262]:


#1--> what is default rate of loans besed on the gender of the applicant 
#2--> how does the income level effect loan aperubel.
#3-->  how does the amoount requested in the prevesus application effect the credit score in  the corrent appication
#4--> what is effent of the contrect type in the prevesh application on  the ligely hood of deafoult
#5-->how does the previous loan behavier loan ammount ,contrecttype,repeayment histry 
# influence the appruval  rate and the loan size in the current   application
# avrage loan amout apuraved application......


# In[263]:


#1.what is the default rate of loans based on the gender of the applicant
gender_default_rate = (df_app.groupby("CODE_GENDER")["TARGET"].mean().reset_index().rename(columns={"TARGET": "DEFAULT_RATE"}))

gender_default_rate["DEFAULT_RATE"] *= 100

gender_default_rate


# In[264]:


#questions
#q1 what is default rate of loans based on the gender of the application?
target_variable_payment_difficulty=df_app[df_app["TARGET"]==1]
male=1
male_1 = (df_app["TARGET"]==1)
male_c=df_app["CODE_GENDER"]=="M"
male_1
male_c
plt.figure(figsize=(10,8))
sns.barplot(x=df_app["CODE_GENDER"],y=df_app["TARGET"],color="blue")
plt.show()


# In[ ]:





# In[ ]:




