# Data Import, Manipulation and Statistics

import pypyodbc
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sci
from pandas import Timestamp
import datetime as dt
import scipy.stats as stats
import researchpy as rp
import statsmodels.api as sm
from scipy import stats
from scipy.stats import norm
from statsmodels.formula.api import ols
from statsmodels.stats.api import anova_lm
from distutils.version import LooseVersion
from sklearn.neighbors import KernelDensity


today = dt.datetime.now()
delta = dt.timedelta(days = 90)
initdate = today - delta

# Establishes connection to SQL Server for Lycra Company

cnxn = pypyodbc.connect('Driver={SQL Server Native Client 10.0};'
                                'Server=MDNEURDS006;'
                                'Database=QDAMDLYC;' 'Trusted_Connection=yes;')
cursor = cnxn.cursor()

# Runs SQL Query that is entered as a string

SQL_Query = pd.read_sql_query("""SELECT a.LIMIT_LOW, a.LIMIT_HIGH, a.AIM, a.DOCUMENTVERSION, b.* FROM 
(
SELECT [ORGANIZATION]
,[PRODUCT_CLASS]
,[PRODUCT_NUMBER]
,[PROPERTY]
,[LIMIT_LOW]
,[LIMIT_HIGH]
,[AIM]
,[DOCUMENTVERSION]
,rank() over (partition by [ORGANIZATION], [PRODUCT_CLASS], [PRODUCT_NUMBER], [PROPERTY] order by [DOCUMENTVERSION] desc) rnk
FROM [TNG.PQM.Operations].[qde].[PROPERTY_LIMITS]
) a,

(SELECT [TEST_RESULT_ID]
,[ORGANIZATION]
,[PRODUCT_CLASS] 
,[PRODUCT_NUMBER]
,[PROPERTY]
,[SAMPLE_TYPE]
,[VESSEL_ONE_NUMBER] as SM
,[VESSEL_TWO_NUMBER] as CELL
,[VESSEL_THREE_NUMBER] as TL
,[TEST_RESULT_VALUE]
,[PRODUCTION_TIME]
,[SEQUENCE_NUMBER]
,[ENTRY_DATE]
,[PROD_RUN_ID]
FROM [QdaMdlyc].[dbo].[TEST_RESULTS]
where PRODUCT_CLASS = 'MERGE'
and PROPERTY in ('TRD','FIN','PRL','CWL','CWS')
and PRODUCT_NUMBER LIKE '1[^Q]%[^R]'
and PRODUCTION_TIME > GETDATE()-90) b
where a.ORGANIZATION = b.ORGANIZATION
and a.PRODUCT_CLASS = b.PRODUCT_CLASS
and a.PRODUCT_NUMBER = b.PRODUCT_NUMBER
and a.PROPERTY = b.PROPERTY
and b.SAMPLE_TYPE = 'R'
and a.rnk = 1;
""", cnxn) 

# Assigns columns for Pandas Dataframe
global df
df = pd.DataFrame(SQL_Query)

# Removes unnecessary columns from Dataframe

to_drop = ['documentversion',
           'test_result_id',
           'organization',
           'product_class',
           'sample_type',
           'sequence_number',
           'entry_date',
           'prod_run_id']
df.drop(columns=to_drop, inplace=True)

# Converts production time column from Daylights Saving to Universal Time

#df.set_index('production_time').resample('D').last().reset_index()
df['production_time']= pd.to_datetime(df['production_time'])

# Removes the whitespace from relevant columns column and standardises cakeweigh

df['product_number'] = df['product_number'].str.strip()
df['sm'] = df['sm'].str.strip()
df['property'] = df['property'].str.strip()
df.loc[(df.property == 'CWL') | (df.property == 'CWS'), 'property'] = 'CW'

# Creates and assigns a Merge-Property and a Merge-Spin Machine-Property column to each row

df['MergeProp'] = df.product_number + " - " + df.property
df['MergeSMProp'] = df.product_number + " - " + df.sm + " - " + df.property

# Creates lists of all the unique Merges, Spin Machines, Properties and Merge-Properties

mergeList = df['product_number'].unique().tolist()
smList = df['sm'].unique().tolist()
propertyList = df['property'].unique().tolist()
uniqueList = df['MergeProp'].unique().tolist()

# Creates a dictionary of pandas tables for each Unique Merge-Property

uniquedict = {elem : pd.DataFrame() for elem in uniqueList}
for key in uniquedict.keys():
    uniquedict[key] = df[:][df.MergeProp == key]