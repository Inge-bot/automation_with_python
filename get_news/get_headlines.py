import variables
import requests

apiKeyVar = variables.api_key

# get headlines from specific country
def get_news(country):
    news_url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={apiKeyVar}"
    r = requests.get(news_url)
    news_content = r.json()
    articles = news_content["articles"]
    news_results = []
    for article in articles:
        # save returned results in the news_result list
        # TODO add proper parsing
        news_results.append(f"Title\n{article['title']}, \nDESCRIPTION\n, {article['description']}")
    return news_results

print(get_news(country="za"))
