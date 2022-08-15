from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

class NewNotesForm(forms.Form):
    note = forms.CharField(label="New Notes")

def index(request):
    if "notes" not in request.session:
        request.session["notes"] = []

    return render(request, "Home/index.html", {
        "notes": request.session["notes"]
    })

def add(request):
    if request.method == "POST":
        form = NewNotesForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data["note"]
            request.session["notes"] += [note]
            return HttpResponseRedirect("/Home")

        else:
            return render(request, "Home/index.html", {
                "form":form
            })

    return render(request, "Home/add.html", {
        "form" : NewNotesForm()
    })