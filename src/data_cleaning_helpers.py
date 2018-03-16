def remove_columns(df, keyword):
    for column_name in df.columns:
        if keyword in column_name:
            df.drop(column_name, axis=1, inplace=True)
    return df

def update_column_names(df, phrase_to_remove, phrase_to_append=''):
    column_list = []
    for column_name in df.columns:
        if phrase_to_remove in column_name:
            column_name = column_name.replace(phrase_to_remove,'') + ' ' + phrase_to_append
        column_list.append(column_name.strip())
    df.columns = column_list
    return df

def add_pct_columns(df, column_names_to_pct, denom_column_name):
    for column_name in column_names_to_pct:
        df[column_name+'%'] = df[column_name]/df[denom_column_name]
    return df

def convert_to_pct_columns(df, column_names_to_pct, denom_column_name):
    for column_name in column_names_to_pct:
        df[column_name] = df[column_name]/df[denom_column_name]
    return df
