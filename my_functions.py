#lower case columns

def lower_case(data, cols= None):
    if cols == None:
        cols = data.columns
    data.rename(columns={col : col.lower() for col in cols}, inplace= True)