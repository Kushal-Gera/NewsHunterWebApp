from django.shortcuts import render
import json
import requests
from basic_app.models import NewsItem

# Create your views here.
# link = "https://newsapi.org/v2/top-headlines?country=us&apiKey=cb9951ac79724fe7a06b2c30afb1d831"
link = "https://newsapi.org/v2/top-headlines?country=us&apiKey=ea6bec1ed711479b9d970525c589ead2"
request_txt = ""
data = {}
newsItemList = []

 =========>>>>>>>>>>>>>>>>>> PLATFORMIO IDE TERMINAL
 =========>>>>>>>>>>>>>>>>>> PLATFORMIO IDE TERMINAL


def index(request):
    global request_txt, data, link, newsItemList
    newsItemList.clear()
    l = 0

    if request.POST: #temporaily changing link to query
        query = str(request.POST['q'])
        if query:
            link = "http://newsapi.org/v2/everything?q=" + query + "&apiKey=ea6bec1ed711479b9d970525c589ead2"


    request_txt = requests.get(link).text
    data = json.loads(request_txt)

    if(str(data["status"]) == "ok"):
        for i in data["articles"]:
            item = NewsItem()

            item.title = i["title"]
            item.desc = i["description"]
            item.full = ""
            if i["content"]:
                item.full = i["content"].split('[')[0]

            img_url = i["urlToImage"]
            if not img_url:
                item.img_url = "https://activated-europe.com/app/uploads/2016/12/the-sand-clock.jpg"
            else:
                item.img_url = img_url

            item.id = l;
            item.link = i["url"]
            item.author = i["source"]["name"]
            item.date = i["publishedAt"].split('T')[0]
            item.writer = str(i["author"])[:20]

            newsItemList.append(item)
            l += 1

    #setting link back to original one !!
    link = "https://newsapi.org/v2/top-headlines?country=us&apiKey=ea6bec1ed711479b9d970525c589ead2"
    return render(request, "basic_app/index.html", {"newsItemList":newsItemList})


def detail(request, id):
    return render(request, "basic_app/detail.html", {"newsItemList" : newsItemList[id]})
