def SMswarm(product_number, property):
    # Swarmplot or Spread of datapoints across each SM
    merged = df.loc[(df.product_number == product_number) & (df.property == property)]
    x = merged['test_result_value']
    sns.set(style="whitegrid")
    ax = sns.swarmplot(y=merged["test_result_value"], x=merged["sm"])

def SMnorm(product_number,property,plot):
    # A histogram and normalised spread of the TRV value for a given merge and property
    merged = df.loc[(df.product_number == product_number) & (df.property == property)]
    if plot == 'spread':
        sns.kdeplot(merged['test_result_value'],label="gaussian distribution",cut=0)
    elif plot == 'cum':
        sns.kdeplot(merged['test_result_value'],label="cumulative frequency",cumulative=True,cut=0)
    else:
        print("Sorry please select a plot type")
    plt.legend()
    
def SMbox(product_number,property):
    #Create a boxplot
    merged = df.loc[(df.product_number == product_number) & (df.property == property)]
    merged.boxplot('test_result_value', by='sm', figsize=(12, 8))

    ctrl = merged['test_result_value'][merged.cell == 'sm']

    grps = pd.unique(merged.sm.values)
    d_data = {grp:merged['test_result_value'][merged.sm == grp] for grp in grps}

    k = len(pd.unique(merged.sm))  # number of conditions
    N = len(merged.values)  # conditions times participants
    n = merged.groupby('sm').size()[0] # Participants in each condition

def SMttest(product_number,property,sm1,sm2):
    #Carries out a two variable t-test on two Spin Machines for a given Merge and Property
    merge = df.loc[(df.product_number == product_number) & (df.property == property)]
    sm1 = merge[merge['sm'] == sm1]['test_result_value']
    sm2 = merge[merge['sm'] == sm2]['test_result_value']
    stats.ttest_ind(sm1, sm2)
    
def Cellbox(product_number,sm,property):
    #Create a boxplot
    merged = df.loc[(df.product_number == product_number) & (df.sm == sm) & (df.property == property)]
    merged.boxplot('test_result_value', by='sm', figsize=(12, 8))

    ctrl = merged['test_result_value'][merged.cell == 'cell']

    grps = pd.unique(merged.cell.values)
    d_data = {grp:merged['test_result_value'][merged.cell == grp] for grp in grps}

    k = len(pd.unique(merged.cell))  # number of conditions
    N = len(merged.values)  # conditions times participants
    n = merged.groupby('cell').size()[0] # Participants in each condition
    
def SMstats(product_number, property, output):
    global k
    k1 = k.filter(['product_number','sm','cell', 'property', 'test_result_value'], axis=1)
    k1 = k1.loc[(k.product_number == product_number) & (k1.property == property)]
    sm_diff = ols('test_result_value ~ product_number + property + sm', data=k1).fit()
    sm_aov_table = sm.stats.anova_lm(sm_diff, typ=1)
    if output == 'table':
        return k1
    elif output == 'diff':
        return sm_diff.summary()
    elif output == 'aov':
        return sm_aov_table
    else:
        print('Sorry output was unclear, please enter again!')

def CELLstats(product_number,spin_mach,property,output):
    global k
    k2 = k.filter(['product_number','sm','cell', 'property', 'test_result_value'], axis=1)
    k2 = k2.loc[(k2.product_number == product_number) & (k2.sm == spin_mach) & (k2.property == property)]
    cell_diff = ols('test_result_value ~ product_number + property + sm + cell', data=k2).fit()
    cell_aov_table = sm.stats.anova_lm(cell_diff, typ=1)
    if output == 'table':
        return k2
    elif output == 'diff':
        return cell_diff.summary()
    elif output == 'aov':
        return cell_aov_table
    
def MergePropTable(Merge,Property):
    x = str(Merge)
    y = str(Property)
    z = x + ' - ' + y
    merged = uniquedict[z]
    return merged
