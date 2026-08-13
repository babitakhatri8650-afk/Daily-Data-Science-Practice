import requests
query="bitcoin"
# query=input("What type of News you want today.")
api="768ae4f379a54df0870a727b6cc22267"
#url=f"https://newsapi.org/v2/everything?q={query}&from=2026-07-06&to=2026-07-06&sortBy=popularity&{api}"
url=f"https://newsapi.org/v2/everything?q={query}&apiKey={api}"
print(url)
r=requests.get(url)
data=r.json()
 
articles=data["articles"]

# for article in articles:
#     print(article["title"],article["url"])
#     #print(article["url"])
#     print("\n**********************************************************************\n")

for index,article in enumerate(articles):
    print(index+1,article["title"],article["url"])
    print("/n**********************************************************************/n")
