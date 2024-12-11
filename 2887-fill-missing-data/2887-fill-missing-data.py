import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # repl = []
    # for i in products['quantity']:
    #     if pd.isna(i):
    #         repl.append(0)
    #         continue
    #     repl.append(i)
    # products['quantity'] = repl
    # return products
    
    # products.quantity.fillna(0, inplace = True)
    products['quantity'].fillna(0, inplace=True)
    return products
    