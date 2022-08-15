from django.http import HttpResponse
from django.shortcuts import render

notes = ["chelsea","arsenal","bournemouth"]

def index(request):
    return render(request, "Home/index.html", {
        "notes": notes
    })

def add(request):
    return render(request, "Home/add.html")