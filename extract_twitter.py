import snscrape.modules.twitter as sntwitter
import nest_asyncio
nest_asyncio.apply()

import pandas as pd
#helper function for scrape tweets data
## subject:keywords for search in twitter; start: tweets which are newer than start_date; end: tweets which are before the end_date
def tweets_seaerch(subject,start,end,num):
    commands=f'{subject} since:{start} until:{end}'
    Tweets_dfsept = []
    # Using TwitterSearchScraper to scrape data and append tweets
    for i,tweetsept in enumerate(sntwitter.TwitterSearchScraper(commands).get_items()):
        if i>num:
            break
        Tweets_dfsept.append(tweetsept)
    Tweets_dfsept2 = pd.DataFrame(Tweets_dfsept)
    # Show Data Frame
    return Tweets_dfsept2