from django.db import models

# Create your models here.

class NewsItem:
    title: str
    desc: str
    img_url:str
    author:str
    date:str
    writer:str

    def __str__(self):
        return self.title;
