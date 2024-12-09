import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    
    # students = students[students['name'].notnull()]
    # return students.loc[students['name'].notna()]
    # return student.loc[students['name'].notnull()]
    return students[students['name'].notnull()]
    # students.dropna(subset = ['name'], inplace = True)
    # return students