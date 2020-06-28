from django.shortcuts import render
import json
import requests
from basic_app.models import NewsItem
# Create your views here.

def index(request):
    link = "https://newsapi.org/v2/top-headlines?country=us&apiKey=cb9951ac79724fe7a06b2c30afb1d831"
    request_txt = requests.get(link).text
    data = json.loads(request_txt)

    newsItemList = []

    for i in data["articles"]:
        item = NewsItem()

        item.title = i["title"]
        item.desc = i["description"]
        img_url = i["urlToImage"]
        if len(img_url) == 0:
            item.img_url = "https://activated-europe.com/app/uploads/2016/12/the-sand-clock.jpg"
        else:
            item.img_url = img_url

        item.author = i["source"]["name"]
        date_str = i["publishedAt"].split('T')[0]
        item.date = date_str
        item.writer = str(i["author"])[0:20]

        newsItemList.append(item)

    return render(request, "basic_app/index.html", {"newsItemList":newsItemList})


def next(request):
    return render(request, "basic_app/next.html")

def settings(request):
    return render(request, "basic_app/settings.html")
