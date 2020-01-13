# Adds a global and unindexed table for stats analysis

global k
k = df

# Creates a table with the count (n) of TRV for each Machine-Merge-Property

n = df.groupby(['product_number', 'sm', 'property'])['test_result_value'].count()

# Creates a table with mean of TRV, Aim, UL and LL for each Machine-Merge-Property

Average = df.groupby(['product_number', 'sm', 'property'])['test_result_value','aim','limit_high','limit_low'].mean()

# Creates a table with standard deviation of TRV

stD = df.groupby(['product_number', 'sm', 'property'])['test_result_value'].std()

# Concatenates the count, average and standard deviation tables into one larger table, then sanitises the data
# by renaming the columns with more intelligible names

results = pd.concat([n, Average, stD], axis=1)

results.columns = ['n', 'Average_TRV', 'Average_Aim', 'Average_UL', 'Average_LL',  'SD_TRV']

# Adds Variance to results dataframe

results['Variance'] = results.SD_TRV * results.SD_TRV

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


results.loc[(results.Cp_Check == True) & (results.CpK_Check == True) & (results.CpM_Check == True), 'Capability'] = 'Good'  
results.loc[(results.Cp_Check == True) & (results.CpK_Check == True) & (results.CpM_Check == False), 'Capability'] = 'Retarget'
results.loc[(results.Cp_Check == True) & (results.CpK_Check == False) & (results.CpM_Check == False), 'Capability'] = 'Adjust Limits'
results.loc[(results.Cp_Check == False) & (results.CpK_Check == False) & (results.CpM_Check == False), 'Capability'] = 'Not Capable'

results.loc[(results.Cp_Check == True) & (results.CpK_Check == True) & (results.CpM_Check == True), 'Capability_Num'] = int(1)  
results.loc[(results.Cp_Check == True) & (results.CpK_Check == True) & (results.CpM_Check == False), 'Capability_Num'] = int(2)
results.loc[(results.Cp_Check == True) & (results.CpK_Check == False) & (results.CpM_Check == False), 'Capability_Num'] = int(3)
results.loc[(results.Cp_Check == False) & (results.CpK_Check == False) & (results.CpM_Check == False), 'Capability_Num'] = int(4)

results = results.reset_index(drop=False)