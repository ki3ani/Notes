from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
notes = ["Had a good time chilling today","Ate sum pizza","went for swimming"]

def index(request):
    return render(request, "Home/index.html", {
        "notes": notes
    })

    