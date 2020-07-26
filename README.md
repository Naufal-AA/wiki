# CS50’s Web Programming with Python and JavaScript
## CS50W Project 1: wiki 
#### for more info [course | CS50W | edx](https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/)

#### Use the app on [Heroku](https://wi-ki.herokuapp.com/)

### Objective

* Become more comfortable with Python.
* Gain experience with Django.

### Background

[Wikipedia](https://www.wikipedia.org/) is a free online encyclopedia that consists of a number of encyclopedia entries on various topics.
Each encyclopedia entry can be viewed by visiting that entry’s page. 
By having one Markdown file represent each encyclopedia entry, we can make our entries more human-friendly to write and edit. When a user
views our encyclopedia entry, though, we’ll need to convert that Markdown into HTML before displaying it to the user.

### Specification

* **Entry Page:** Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.

* **Index Page:** Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.

* **Search:** Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring.
Clicking on any of the entry names on the search results page should take the user to that entry’s page.

* **New Page:** Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
Users should be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.
Users should be able to click a button to save their new page.
When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.
Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.

* **Edit Page:** On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
The textarea should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).
The user should be able to click a button to save the changes made to the entry.
Once the entry is saved, the user should be redirected back to that entry’s page.

* **Random Page:** Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.

* **Markdown to HTML Conversion:** On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user. 


### Requirements
* <img src="https://avatars1.githubusercontent.com/u/27804?s=400&v=4" width="25" valign="middle"> Django

### :gear: Terminal 

```cmd
# Install necessary packages
> pip3 install Django==3.0.8
> pip3 install markdown2

#create a project 
> django-admin startproject wiki

#Create app in project in wiki
> python manage.py startapp encyclopedia

#make migration 
> python manage.py migrate

#run Program
> python manage.py runserver 
```

# Wiki

 <img src="https://i.ibb.co/KsfDyJR/1.png" width="450" valign="abs-middle">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://i.ibb.co/Xt1F0ft/2.png" width="450" valign="abs-middle">   
 ------------------------
 
 <img src="https://i.ibb.co/2kSHtWw/3.png" width="450" valign="abs-middle">&nbsp;&nbsp;&nbsp;<img src="https://i.ibb.co/VJSNDws/4.png" width="450" valign="abs-middle"> 
 ===============

