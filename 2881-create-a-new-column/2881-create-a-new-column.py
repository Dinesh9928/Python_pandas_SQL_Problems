import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    
    # employees['bonus'] = employees.apply(lambda x:x['salary']*2,axis=1)
    
    # return employees.assign(bonus = employees['salary'] * 2)
    
    # return employees.assign(bonus=lambda x: x.salary * 2)
    
    employees['bonus'] = employees['salary']*2
    
    

    return employees