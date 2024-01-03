import yagmail
import pandas as pd
from news import NewsFeed
import datetime
import time

while True:
    if datetime.datetime.now().hour == 15 and datetime.datetime.now().minute == 11:
        df = pd.read_excel('people.xlsx')

        today = datetime.datetime.now().strftime('%Y-%m-%d')
        yesterday = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        for index, row in df.iterrows():
            news_feed = NewsFeed(interest=row['interest'], from_date=yesterday,
                                 to_date=today)
            email = yagmail.SMTP(user="#Use your Email", password="# Use the Google Apps Password")
            email.send(to=row['email'],
                       subject=f"Your {row['interest']} news for today",
                       contents=f"Hi {row['name']}\n , See what is on about "
                                f"{row['interest']} today.\n"
                                f"{news_feed.get()}"
                                f"This is the Body of the Email"
                               "This is the Python Programming Course",
                       attachments="design.png")
    time.sleep(60)

# Note
# Need to enter your emai in the user ="#Use your Email" and the Google Apps Password
# In the people.xlsx, there is a need to enter the email that you want to send to
# and also indicate the interest to invoke the row['interest'] here.
# Download the yagmail in the Python Library.



