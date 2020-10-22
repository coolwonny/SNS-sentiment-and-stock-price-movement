# Project 3 - NLP Analysis and Stock Data
## Alex Waters, Joe Swiderski, Marcus Kim, Mark Foxworth, Zach Cone
## October 20, 2020

---

## MOTIVATION AND SUMMARY

The goal of the project was determine if there is any correlation between the text sentiment of a given stock and the stock’s price movement.  

The project utilized various text sources such as comment threads from Yahoo Finance and Reddit, Twitter posts, and news articles to examine sentiment utilizing various machine learning models.  

This sentiment analysis was compared to stock price movements over time, including daily stock price movements and intertrade day movements, to review any possible correlation in the data. 
 The project focused on information related to Tesla with the intent to apply the same methodology to other stocks assuming any correlation was found.   

---
## QUESTIONS OF THE DATA

 1.  Is there a correlation between stock price movements and sentiment related to comments on yahoo finance, twitter, reddit, and news sources?
 
 2. Does Elon Musk Twitter comments drive the stock price more than social media?

 3. Can various comments and news articles be used to predict the movements of a stock price?
---
## DATA SOURCES, PACKAGES, and ANAYSIS METHODS

### *Data Sources*

- Yahoo Finance Comment Threads:  1 month, daily, 11,467
- Twitter Elon Musk: 3 yrs, dy/hr/min, 6906
- Twitter Tesla Company:  4 yrs, daily, 785
- Twitter "Tesla Price": 6 months, dy/hr/min, 41430
- Reddit "Tesla" Threads:  3 yrs, dy/hr/min, 2,253,039
 - Reuters news:  4 yrs, daily, 1321
 - News Articles via News API: 1 month, daily, 612

### *Python Packages*

- Sklearn
- BeautifulSoup
- Selenium
- News API
- NLTK
- Pandas
- Reddit API
- Numpy
- Plotly
- PRAW
- Yahoo Finance (Python)
- TextBlob
- TensorFlow

### *Analysis Methods*

- Visualizations using plots
- Train/Test methods
- Data frames
- Possible text tokenization
- Loops
- Sentiment Analysis
- Algorithmic trading

---
## Historical Stock Price
![tesla trad history: hourly, 2 years](Images/Hourly_Stock_History.PNG)
Tesla Trade History: Hourly (2 years)

---   
## *Twitter Data*
     
### [Elon Musk Tweets / Retweets](https://github.com/coolwonny/project-3/blob/main/Resources/Elon_Musk_tweets_cst_final.csv)
- https://twitter.com/elonmusk
- 01/01/2018 to 10/12/2020
- More SpaceX topics recently

### [Tesla Company Tweets](https://github.com/coolwonny/project-3/blob/main/Resources/tesla_tweets.csv)
- https://twitter.com/tesla 
- 11/16/2016 to 09/23/2020
- Less tweets in 2020

### [Mass Tweets on Tesla Price](https://github.com/coolwonny/project-3/blob/main/Resources/concat_query_tesla_price_final.csv)
- https://twitter.com/search?q=tesla%20price%20lang%3Aen%20until%3A2020-10-13%20since%3A2020-04-30&src=typed_query&f=live
- 05/01/2020 to 10/13/2020
- Search by 'Tesla Price'
- Limitation on page scrolls per hour by Twitter    
  (Optimized scroll rate without errors = 925 pixels every 5 seconds of timesleep)

---


## *Reddit Data*

### Pushshift Reddit API
- https://github.com/pushshift/api
- q=‘TSLA|tesla’
- 01/01/2018
- 100 records per fetch
- 429 error – Too Many Requests

### Subreddits
- wallstreetbets
- stocks
- investing
- StockMarket
- CryptoCurrency

### PRAW
- Library
- inflexible
---   
## *Yahoo Finance Data*    

### Tesla Stock Price (yfinance python)
 - Adjusted price after stock-split
 - Intervals available by [daily](https://github.com/coolwonny/project-3/blob/main/Resources/Daily_Stock_Data_4_Yrs.csv), [hourly](https://github.com/coolwonny/project-3/blob/main/Resources/Hourly_Data_by_year.csv) and minutes(5 min / [15 min](https://github.com/coolwonny/project-3/blob/main/Resources/fifteen_min_for_sixty_day.csv) / 30 min)
 - Limitations: hourly price up to 730 trading days, minutes price up to 60 trading days

### [Yahoo Finance Conversations](https://github.com/coolwonny/project-3/blob/main/Resources/Yahoo_conversations_cst.csv)
- https://finance.yahoo.com/quote/TSLA/community?p=TSLA
- 09/23/2020 to 10/09/2020
- Filtered by 'Recently Discussed'
- Dynamic pages ("Show More" button)  
- Timestamp not provided. Only with 'XX minutes/hours/days/months ago'

---
## *Reuters / News API Data*    

### [Reuters headlines and articles](https://github.com/coolwonny/project-3/blob/main/Resources/Tesla_reuter_full.csv)
 - https://www.reuters.com/companies/TSLA.OQ/news
 - The most recent four years
 - Returns headlines and bodies separately
 - Timestamp not provided. Only with 'XX hours/days/months/years ago'

### [News API articles](https://github.com/coolwonny/project-3/blob/main/Resources/tsla_newsapi.csv)
 - Limits on free version: up to current 30 days 
---

## *Twitter Analysis*

1. Decide which TSLA Price we use Daily / Hourly / 15 minutes

2. Preparing for various Sentiment Score Subjectivity and Polarity scores from TextBlob Going straight with Polarity score only Or tweaking and combining with Subjectivity score by filtering or weighting Simply taking more objective texts only (i.e. dropping out texts w/ Subjectivity > 0.4) Creating adj. Polarity score by weighting on subjectivity If  0 <= Subjectivity score <= 0.2  ⇒ 140% * Polarity score 0.2< Subjectivity score <= 0.4  ⇒ 120% * Polarity score and so on. Grouping scores by daily/hourly/15 mins by taking mean, sum, count, first and last
 
3.  Comparing the analysis by market hours
Analyze all texts regardless of on and off market hours or
Analyze only texts posted within market hours 

Tesla Tweets Market Hours Only
![mass tweets on tesla price, hourly, 6 months](Images/heatmap_tweets_TSLA_price_dropHighSubjectivity_market_hours_only.png)

Tweets on tesla price:dropped hight subjectivity, market hours only
![analysis method cont](Images/plot_tweets_TSLA_price_dropHightSubjectivity_all_hours.png)

Tweets on TSLA Price: dropped high subjectvity, market hours only left to right top to bottom:hour price, hourly price change, polarity count score, polarity count change
![anaylsis method cont](Images/plot2_tweets_TSLA_price_dropHightSubjectivity_market_hours_only.png)

Hourly return vs Polarity Mean Change(dropped high subjectivity)
![analysis method cont](plot_ElonMusk_dropHighSubjectivity_market_hours_only_return_vs_mean_change.png
)
Hourly Price vs Polarity count(dropped high subjectivity- market hours only)
![mass tweets on tesla price, hourly, 6 months](Images/plot_TeslaPrice_dropHighSubjectivity_market_hours_only_price_vs_count.png)

There was a relatively strong correlation between hourly price change and the number of comments (corr=0.30) for mass tweets on the tesla price. 
---
## *Reddit Analysis*

![reddit anaylsis](Images/Reddit_Heat_Map.PNG)

![reddit heat map](Images/heatmap_Reddit_dropHighSubjectivity_market_hours.png)

![reddit plot](Images/plot_Reddit_dropHighSubjectivity_market_hours_only_price_vs_count.png)

Filtered Reddit data by wallstreetbets subreddit
Added the hourly Tesla stock price infor for the last two years to the dataframe.
Dropped null values and additional columns not needed. 
161,643 rows of data (test and stock movement)

*Findings:*

Some correlation between polarity counts (or number of posts) and stock Price (.66). 

Comparing this to the Elon Musk tweets, we found that the number of texts counts on TSLA’s hourly price had the strongest correlation. 

---

## *Twitter RNN_LSTM Conclusion*

![accuracy score](Images/LTSM_Accuracy_Score.PNG)

![classification report](Images/LTSM_Classification_Report.PNG)

Took Twitter text data and combined it with the movement, either up or down. 
Ran this through an LSTM model to see how accurate it could be at predicting stock movement based on Tweets from Twitter. 

Conclusion is the model was only accurate 52% of the time.

---

## *Word Cloud Visualizations*

Tesla Price Tweets
![wordcloud](Images/tesla_price_tweets_wordcloud.PNG)
Tesla Reuters Headlines
![wordcloud](Images/tesla_reuters_headline_wordcloud.PNG)
Tesla Reuters Text
![wordcloud](Images/tesla_reuters_text_wordcloud.PNG)
Tesla Yahoo Finance
![wordcloud](Images/yahoo_finance_wordcloud.PNG)

---

## **WRAP UP AND OUTSTANDING QUESTIONS**

1. Review and testing of the “aftermarket” text data may provide additional lead indicators for next days opening.  
2. Is the sentiment score from TextBlob and Vader reliable enough to find any real correlations with the stock price? We observed not a few texts that weren’t classified correctly. 
3. For twitter, the API had a restriction on days(7 days), and web crawling also had a limit on the pages shown at a given period of a time, which made us difficult to get sufficient data. 
4. More time needed to clean the reddit data.  Reddit contained many posts that were noise and junk.
