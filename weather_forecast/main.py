import variables
import requests

apiKeyVar = variables.api_key

# Http request
response = requests.get(f"https://newsapi.org/v2/everything?qInTitle=Twitter lets the certificate for its Tor onion site expire, effectively killing off the privacy- and speech-protecting service a year after it launched&from=2023-03-08&sortBy=popularity&apiKey={apiKeyVar}")
# return a JSON object of the result (if result is in the JSON format already)
content = response.json()

# use debugger to make the content more readable
# print(content)

# save to var 
articles = content["articles"]
print(type(articles))

# loop through and print certain article fields
for article in articles:
    print("\nTITLE\n", article["title"], "\nDESCRIPTION\n", article["description"], "\nCONTENT\n", article["content"])
print(type(content))
# print(content["articles"][0]["title"])
