def inpute_data(df):
    '''Inputing NaN data'''
    df_copy = df.copy() #Copy so as not to change the original
    
    #Inputing NaN categorical values with column mode
    categorical_vars = list(df_copy.select_dtypes(include=["object"]).columns)
    for col in categorical_vars:

        if (df_copy[col].isnull().values.any()):
            df_copy[col].fillna(df_copy[col].mode()[0], inplace=True)
    

    #Inputing NaN numerical values with column median
    numerical_vars = list(df_copy.select_dtypes(include=["int64", "float64"]).columns)
    for col in numerical_vars:

        if (df_copy[col].isnull().values.any()):
            df_copy[col].fillna(df_copy[col].median(), inplace=True)
    

    return df_copy
