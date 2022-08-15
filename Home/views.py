from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms

# Create your views here.

class AddNote(forms.Form):
    note = forms.CharField(label="New Note")


def index(request):
    if "notes" not in request.session:
        request.session["notes"] = []

    return render(request, "Home/index.html", {
        "notes": request.session["notes"]
    })

