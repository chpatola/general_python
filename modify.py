#Function for renaming columns & checking the result
def nyName (old,new,pd):
    print(pd.columns)
    pd.rename(columns={old: new}, inplace = True)
    print(pd.columns)