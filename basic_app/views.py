from django.shortcuts import render
import json
import requests
from basic_app.models import NewsItem

# Create your views here.
link = "https://newsapi.org/v2/top-headlines?country=us&apiKey=cb9951ac79724fe7a06b2c30afb1d831"
request_txt = requests.get(link).text
data = json.loads(request_txt)
newsItemList = []

def index(request):
    l = 0

    for i in data["articles"]:
        item = NewsItem()

        item.title = i["title"]
        item.desc = i["description"]
        item.full = i["content"]
        img_url = i["urlToImage"]
        if not img_url:
            item.img_url = "https://activated-europe.com/app/uploads/2016/12/the-sand-clock.jpg"
        else:
            item.img_url = img_url

        item.id = l;
        item.link = i["url"]
        item.author = i["source"]["name"]
        item.date = i["publishedAt"].split('T')[0]
        item.writer = str(i["author"])[0:20]

        newsItemList.append(item)
        l += 1

    return render(request, "basic_app/index.html", {"newsItemList":newsItemList})


def detail(request, id):
    return render(request, "basic_app/detail.html", {"newsItemList" : newsItemList[id]})

def next(request):
    return render(request, "basic_app/next.html")

def settings(request):
    return render(request, "basic_app/settings.html")
