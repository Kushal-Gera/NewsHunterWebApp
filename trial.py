import json
import requests

link = "https://newsapi.org/v2/top-headlines?country=us&apiKey=cb9951ac79724fe7a06b2c30afb1d831"

request = requests.get(link)
req_text = request.text

data = json.loads(req_text)

desc_list = []
title_list = []
articles = {"articles" : {"title_list":title_list, "desc_list":desc_list}}

# for i in data["articles"]:
    # articles["articles"]["title_list"].append(i["title"])
    # articles["articles"]["desc_list"].append(i["description"])

# length = len(articles["articles"]["title_list"])

kushal = "kushal"
x = 5

def fun():
    global kushal,x
    kushal = "hey"
    x = 6

print(kushal)
fun()
print("**********************")
print(kushal, x)

# for a in range(length):
    # print(articles["articles"]["title_list"][a])
    # print("**********************")
