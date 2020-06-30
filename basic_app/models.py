from django.db import models

# Create your models here.

class NewsItem:
    title: str
    desc: str
    full: str
    img_url:str
    author:str
    date:str
    writer:str
    id = 0
    link:str

    def __str__(self):
        return self.title;
