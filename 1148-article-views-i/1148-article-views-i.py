import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    mask = (views['author_id'] == views['viewer_id'])

    unique_ids = (
        views.loc[mask, 'author_id'].drop_duplicates().sort_values()
    )

    return pd.DataFrame({'id': unique_ids}) # converting dictionary to dataframe
    