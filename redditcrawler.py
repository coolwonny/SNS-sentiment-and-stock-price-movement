import requests
import pandas as pd
import time
from datetime import datetime, timezone, timedelta
DELIMITER = chr(255)        # csv delimiter

# encapsulate pushshift api
def get_pushshift_data(data_type, **kwargs):
    # https://github.com/pushshift/api
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    request = requests.get(base_url, params=kwargs)
    return request.json()

# get the cursor format required by pushshift
def get_cursor(time_shift):
    return "%s%s" % (int(time_shift), 's')

# day_to_process. starting crawl day. starting time of 11:59:59 PM. Note code crawls backwards in time
dtp = datetime(2020, 6, 20, 23, 59, 59, tzinfo=timezone.utc)

'''
Reddit maximum return is 100 comments. move the "cursor" to the next set of records to get around Reddit maximum
'''
while dtp.year > 2017:
    df1 = None
    cursor = get_cursor(datetime.now().timestamp() - dtp.timestamp())

    # loop until the previous day is hit
    while True:
        try:
            # get Reddit data
            data = get_pushshift_data(data_type="comment", q="TSLA|tesla", size=100, before=cursor).get("data")
        except:
            # sleep for 5 seconds and try again
            print('!!!!!     429 Error...sleeping     !!!!!')
            time.sleep(5)
            continue
        # sleep to get around Reddit 429 "Too Many Requests"
        time.sleep(0.3)
        # load the results into dataframe
        df2 = pd.DataFrame.from_records(data)[["author", "subreddit", "created_utc", "body", "id"]]
        # append current results to overall results
        df1 = pd.concat([df1, df2])
        # if we've gone past the current day, break
        last_record = datetime.utcfromtimestamp(int(df1.tail(1).created_utc))
        if last_record.day != dtp.day: break
        # move the cursor past the last record
        cursor = get_cursor(datetime.now().timestamp() - df1.tail(1).created_utc)
        

    # convert epoch seconds to readable timestamp
    df1.created_utc = df1.created_utc.apply(lambda x: datetime.utcfromtimestamp(x))
    # remove newlines from the comment body
    df1.body = df1.body.apply(lambda x: x.replace('\n', ' ').replace('\r', ''))
    # only use results for the current day
    df = df1.loc[df1['created_utc'].dt.day == dtp.day]
    # write to file
    print(df.tail())
    df.to_csv(f"./data/TSLA_tesla_{dtp.strftime('%Y_%m_%d')}.csv", sep=DELIMITER, index=False, encoding="utf-8")
    # decrement the day for the next pass
    dtp = dtp + timedelta(days=-1)
