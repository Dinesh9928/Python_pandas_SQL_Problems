import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(
    columns = {
        "id": "student_id",
        "first": "first_name", 
        "last": "last_name",
        "age": "age_in_years",
        },
        inplace = True
    )
    # students.rename(
    #     {
    #         'id': 'student_id',
    #         'first': 'first_name',
    #         'last': 'last_name',
    #         'age': 'age_in_years'
    #     },
    #     axis=1,
    ##.   axis='columns',
    #     inplace=True
    # )
    
   
    return students
    