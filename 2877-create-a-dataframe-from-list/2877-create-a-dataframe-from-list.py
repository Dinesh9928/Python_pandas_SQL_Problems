import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(
    {
        "student_id": [item[0] for item in student_data],
        "age": [item[1] for item in student_data]
    }
    )