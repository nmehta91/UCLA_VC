__author__ = 'nitishmehta'
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
import urllib2
import json
from flask.ext.pymongo import PyMongo
from pymongo import MongoClient
from User import *

app = Flask(__name__)
# You need to have a Mongo DB instance running on your computer having a database name as VC_FUND
app.config['MONGO_URI'] = 'mongodb://localhost:27017/VC_FUND'
mongo = PyMongo(app)

@app.route('/')
def mainpage():
    # Please add the appropriate access token before running this code
    url = "https://api.angel.co/1/search?query=ucla&type=User&access_token="
    response  = urllib2.urlopen(url)
    user = json.loads(response.read())

    client = MongoClient()
    db = client.VC_FUND
    posts = db.posts

    # Please add the appropriate access token before running this code
    for u in user:
        url = "https://api.angel.co/1/users/"+ str(u['id']) +"?access_token="
        response  = urllib2.urlopen(url)
        job = json.loads(response.read())
        if mongo.db.posts.find_one({'id': job['id']}) != None:
            continue
        posts.insert(job)

    users = mongo.db.posts.find()

    usersList = []

    for u in users:
        location = None
        if len(u['locations']) > 0:
            list = str(u['locations']).split(',')
            stri  = str(list[2]).index(':')
            location = list[2][stri+4:len(list[2])-1]

        userObj = User(name=u['name'], image=u['image'], location=location, twitter_url=u['twitter_url'], facebook_url=u['facebook_url'], github_url=u['github_url'], bio=u['bio'], angellist_url=u['angellist_url'], what_ive_built=u['what_ive_built'], linkedin_url=u['linkedin_url'], criteria=u['criteria'], blog_url=u['blog_url'], investor=u['investor'], skills=u['skills'])
        usersList.append(userObj)


    return render_template('mainpage.html', users = users, usersList = usersList)


if __name__ == '__main__':
   app.debug = True
   app.run()




