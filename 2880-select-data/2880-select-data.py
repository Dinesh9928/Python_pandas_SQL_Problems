import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # return students.loc[students['student_id'] == 101, ['name', 'age']]
    # return students.loc[students["student_id"] == 101, "name" :]
    # return students[students.student_id==101][['name','age']]
    df = students[students['student_id'] == 101]
    return df[['name','age']]
    