from django.http import HttpResponse
from django.shortcuts import render
from django import forms

notes = ["chelsea","arsenal","bournemouth"]

class NewNotesForm(forms.Form):
    note = forms.CharField(label="New Notes")

def index(request):
    return render(request, "Home/index.html", {
        "notes": notes
    })

def add(request):
    if request.method == "POST":
        form = NewNotesForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data["note"]
            notes.append(note)

        else:
            return render(request, "Home/index.html", {
                "form":form
            })

    return render(request, "Home/add.html", {
        "form" : NewNotesForm()
    })