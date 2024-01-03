# API Key: Get API Keys from newsapi.org
import requests
from pprint import pprint


class NewsFeed:
    """Multiple News Titles and the links as the Single String"""
    base_url = "http://newsapi.org/v2/everything?"
    api_key = "Get API Keys from newsapi.org"

    def __init__(self, interest, from_date, to_date, language="en"):
        self.interest = interest
        self.from_date = from_date,
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&language={self.language}&" \
              f"to={self.to_date}&" \
              f"apiKey={self.api_key}"

        response = requests.get(url)
        # Convert the data into the Dictionary:
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body


# If this file is running as the main file:
if __name__ == "__main__":
    news_feed = NewsFeed(interest="nasa", from_date="2023-11-6", to_date="2023-11-14",
                         language="en")
    print(news_feed.get())

# Note
# Need to get the API key from the http://newsapi.org website URL
