# CollabLab-Flask-basic
Meant to be a set of base code for CollabLab research assistants to use for developing web apps.  Please fork this app and update as needed.  If you don't know how to update something from the original repository, follow [these instructions to add an "upstream" link to this repository](https://help.github.com/articles/syncing-a-fork/) and [these instructions to fetch from this repository](https://help.github.com/articles/configuring-a-remote-for-a-fork/).

You will need to have the following installed in order to use this:
* Python
  * [Flask](http://flask.pocoo.org)

## Installing Flask

If python and pip are installed, you should be able to simply type the following command
```sudo pip install flask```

---

This repo is divided up into a few different apps that are each boiler plates for different kinds of projects.  These projects are find in the various "app1","app2",... folders.

---

## /app1 : Serving static content

This is app is here just to show the general idea behind flask and to use as a quick way to serve content locally on your computer.  None of this is necessary if you have a webserver like apache or nginx running on your computer, but those can take some time and expertise to install and setup.

### How to serve static content with /app1
1. Put all the static content into /static/css, /static/js and /static/static_html folder
2. run the flask server by typing ```python run.py``` from the /app directory
3. The flask app uses the IP address 127.0.0.1:5000 by default, so type that address into your browser and you should see your page.
4. 

<b><i>Pro Tip : You may need to type "http://" before the IP address.  Some browsers will not know that your intention is to make an http request for a webpage"</i></b>

## /app2 : Database integration with SQLite
This is app is here to show how you can integrate flask with a database running on your computer.  SQLite is good for proof of concept, but for live websites with a fair amount of data to track you should be using either PostgreSQL or MongoDB.

*implementation details to come*

