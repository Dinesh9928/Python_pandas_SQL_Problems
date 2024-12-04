

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.loc[0:2]


#      import pandas as pd
#      def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#         return employees.head(3)

#      def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#         return employees.loc[0:2]

#      def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#         return employees[:3]
 


