import pypyodbc
import numpy as np
import pandas as pd
import math

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
and PROPERTY in ('TRD','FIN','PRL','CWL', 'CWS')
and PRODUCT_NUMBER LIKE '1A2%[^R]'
and PRODUCTION_TIME > GETDATE()-1) b
where a.ORGANIZATION = b.ORGANIZATION
and a.PRODUCT_CLASS = b.PRODUCT_CLASS
and a.PRODUCT_NUMBER = b.PRODUCT_NUMBER
and a.PROPERTY = b.PROPERTY
and b.SAMPLE_TYPE = 'R'
and a.rnk = 1;
""", cnxn) 

# Assigns columns for Pandas Dataframe

df = pd.DataFrame(SQL_Query)

# Adds a Unique Column in the format 'product_number - sm - property'

df = df.set_index(['product_number', 'sm', 'property'])

# Creates a pivot table with the count (n) of TRV for each Machine-Merge-Property

n = df.pivot_table(index=['product_number', 'sm', 'property'],values=['test_result_value'], aggfunc='count')

# Creates a pivot table with mean of TRV, Aim, UL and LL for each Machine-Merge-Property

AveragePivot = df.pivot_table(index=['product_number', 'sm', 'property'],values=['test_result_value','aim','limit_high','limit_low'], aggfunc='mean')

# Creates a pivot table with standard deviation of TRV

stDPivot = df.pivot_table(index=['product_number', 'sm', 'property'],values=['test_result_value'],aggfunc='std')

# Concatenates the count, average and standard deviation tables into one larger table, then sanitises the data
# by renaming the columns with more intelligible names

results = pd.concat([n, AveragePivot, stDPivot], axis=1)

results.columns = ['n', 'Average_Aim', 'Average_UL', 'Average_LL', 'Average_TRV', 'SD_TRV']

# Adds Limit Difference to results dataframe: Upper Limit - Lower Limit

results['LimDiff'] = results.Average_UL - results.Average_LL

# Adds Cp to results dataframe: Cp = Limit Difference / (6 * Standard Deviation of TRV)

results['Cp'] = (results.LimDiff / (6 * results.SD_TRV))

# Adds CpKU, CpKL and CpK to results dataframe: 
# CpKU = (Average Upper Limit - Average TRV) / (3 * results.SD_TRV) 
# CpKL = (Average Lower Limit - Average TRV) / (3 * results.SD_TRV)
# CpK = CpKU - CpKL

results['CpKU'] = ((results.Average_UL - results.Average_TRV)/(3 * results.SD_TRV))
results['CpKL'] = ((results.Average_TRV - results.Average_LL)/(3 * results.SD_TRV))
results['CpK'] = results[['CpKU','CpKL']].min(axis=1)

# Calcuates (grand average - process target), then the denominator for the CpM calculation and finally CpM

results['TV_SR'] = (results.Average_TRV - results.Average_Aim)
results['CpM_Denominator'] = (1+((results.TV_SR)**2)/((results.SD_TRV)**2))**0.5
results['CpM'] = results.Cp / results.CpM_Denominator

# Adds the Aims for each process capability value to the table

results['Cp_Aim'] = 1.33
results['CpK_Aim'] = 1.33
results['CpM_Aim'] = 1.33

# Adds a check for each process capability value against the aim

results['Cp_Check'] = np.where(results['Cp'] >= results['Cp_Aim'], True, False)
results['CpK_Check'] = np.where(results['CpK'] >= results['CpK_Aim'], True, False)
results['CpM_Check'] = np.where(results['CpM'] >= results['CpM_Aim'], True, False)