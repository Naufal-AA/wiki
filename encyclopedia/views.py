
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

from . import util
from markdown2 import Markdown
import secrets


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Enter a title", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8','autocomplete' : 'off','autofocus' : 'autofocus' ,'placeholder' : 'Title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control col-md-8 col-lg-8', 'rows' : 10,'placeholder' : 'Content','autocomplete' : 'off','autofocus' : 'autofocus'}))
    edit = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)
    
def index(request):
	context = {
		"entries" : util.list_entries()
	}
	return render(request, "encyclopedia/index.html", context)

def entry(request, entry):
    markdowner = Markdown()
    entryPage = util.get_entry(entry)
    if entryPage is None:
    	context = {
    		"title" : entry ,
    		"error" : "Sorry! There were no result matching the query"
    	}
    	return render(request, "encyclopedia/title.html", context)

    else:
    	context = {
    		"title" : entry , 
    		"entry" : markdowner.convert(entryPage)
    	}
    	return render(request, "encyclopedia/title.html" , context)

def new_page(request):
    if request.method == "POST":
        mode = False
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if (util.get_entry(title) is None or form.cleaned_data["edit"] is True):
                util.save_entry(title,content)
                return HttpResponseRedirect(reverse("entry", args=(title,)))
            else:
            	context = {
            		"form" : form ,
            		"message" : "The name is already exist!"
            	}
            	return render(request, "encyclopedia/entry.html", context)
    else:
	    return render(request,"encyclopedia/entry.html", {
	        "form": NewEntryForm()
	    }) 
       
def edit(request, entry):
	entryPage = util.get_entry(entry)
	if entryPage is None:
		message = "sorry! File \"" + entry + "\" does not exist"
		context = {
			"title" : entry ,
			"mode" : True,
			"message" : message
		}
		return render(request, "encyclopedia/entry.html", context)
	else:
		form = NewEntryForm()
		form.fields["title"].initial = entry
		form.fields["title"].widget = forms.HiddenInput()
		form.fields["edit"].initial = True
		form.fields["content"].initial = entryPage
		return render(request, "encyclopedia/entry.html",{
				"mode" : True,
				"form" : form ,
				"title" : form.fields["title"].initial
			})


def random(request):
	entries = util.list_entries()
	Entries = secrets.choice(entries)
	return HttpResponseRedirect(reverse("entry", args=(Entries,)))


def search(request):
    keyword = request.GET.get('q')
    search = keyword.lower()
    entries = util.list_entries()

    substr = []

    for s in entries:
        word = s.lower()
        if(word.find(search) != -1):
            substr.append(s)

    if len(substr) != 0 :
        message = "Search Result found for \"" + keyword + "\""
        context = {
            "entries" : substr ,
            "message" : message ,
            "search" : True
        }
        return render(request, "encyclopedia/index.html", context)

    else:
        message = "Sorry! No result Found for \"" + keyword + "\""
        context = {
            "message" : message ,
            "search" : True ,
            "create" : keyword,

        }
        return render(request, "encyclopedia/index.html", context)






