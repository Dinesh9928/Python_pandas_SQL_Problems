# import pandas as pd

# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     return pd.DataFrame(
#     {
#         "student_id": [item[0] for item in student_data],
#         "age": [item[1] for item in student_data]
#     }
#     )

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    column_names = ["student_id", "age"]
    result_dataframe = pd.DataFrame(student_data, columns=column_names)
    return result_dataframe