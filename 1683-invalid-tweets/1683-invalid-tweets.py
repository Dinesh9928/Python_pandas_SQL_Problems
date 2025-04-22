import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    mask = (tweets['content'].str.len() > 15)
    return tweets.loc[mask, ['tweet_id']]
    # res = tweets.loc[tweets.content.str.len()>15]
    # return res[['tweet_id']]
    