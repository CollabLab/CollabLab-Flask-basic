# CollabLab-Flask-basic
Meant to be a set of base code for CollabLab research assistants to use for developing web apps.  Please fork this app and update as needed.  If you don't know how to update something from the original repository, [this is a great blog on how to set that up](http://bradlyfeeley.com/2008/09/03/update-a-github-fork-from-the-original-repo/) so that you can update your project with any new developments from us.

You will need to have the following installed in order to use this:
* Python
  * [Flask](http://flask.pocoo.org)

## Installing Flask
If python and pip are installed, you should be able to simply type the following command
```sudo pip install flask```

## Serving static content

1. Put all the static content into the appropriate /static/css, /static/js and /static/static_html folder
2. run the flask server by typing ```python run.py``` from the /app directory
3. The flask app uses the IP address 127.0.0.1:5000 by default, so type that address into your browser and you should see your page.

<b><i>Pro Tip : You may need to type "http://" before the IP address.  Some browsers will not know that your intention is to make an http request for a webpage"</i></b>
