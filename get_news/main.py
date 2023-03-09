import variables
import requests

apiKeyVar = variables.api_key

def get_news(news_topic, from_date, to_date, lang):
    news_url = f"https://newsapi.org/v2/everything?qInTitle={news_topic}&from={from_date}&to={to_date}&sortBy=popularity&language={lang}&apiKey={apiKeyVar}"
    r = requests.get(news_url)
    news_content = r.json()
    articles = news_content["articles"]
    news_results = []
    for article in articles:
        # save returned results in the news_result list
        news_results.append(f"Title\n,{article['title']}, \nDESCRIPTION\n, {article['description']}")
        return news_results

print(get_news(news_topic="pie", from_date="2023-03-08", to_date="2023-02-09", lang="en"))
