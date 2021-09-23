import os

from django.shortcuts import render


# Create your views here.
def base(request):
    return render(request, 'base.html')


def index(request):
    images = [{
        'title': "MSRA",
        "body": "Life at Microsoft Research Asia (2021)"
    }, {
        'title': "Amazon",
        "body": "SDE Intern at Amazon (Summer 2020)"
    },{
        'title': "UCLA",
        "body": "Life in UCLA. Go Bruins!!"
    },{
        'title': "Beijing",
        "body": "Life in Beijing"
    },

    ]

    whatsnew = [{
        "time": "Sept. 17th, 2021",
        "desc": "I completed my internship at Microsoft Research Asia (MSRA)",
    }, {
        "time": "Sept. 15th, 2021",
        "desc": "I wrote a help doc for incoming interns at MSRA SC Group. You can read part of it from <a>here</a>",
    }, {
        "time": "Dec. 22th, 2020",
        "desc": "I started to work as a research intern at MSRA",
    },{
        "time": "Sept. 4th, 2020",
        "desc": "I completed my SDE internship at Amazon (FBA IAR Team)",
    },
    ]

    research = None

    context = {
        "images": images,
        "whatsnew": whatsnew,
    }
    return render(request, 'index.html', context)

def detail(request, topic):
    imgs = os.listdir(f"static/{topic}")
    imgs = [img.split(".jpg")[0] for img in imgs]
    imgs = [img for img in imgs if img[0:2] != "IMG"]
    imgs.remove("0")

    context = {
        "topic": topic,
        "images": imgs
    }
    return render(request, 'gallery/detail.html', context)
