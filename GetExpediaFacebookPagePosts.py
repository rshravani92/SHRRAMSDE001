# program to extract last n posts on company facebook page

import urllib2
import json
import datetime

company = 'expedia'
numberOfPosts = 8

# function to get data from facebook graph API
def getDataFromGraphAPI(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = json.loads(response.read())
    return  data

# Following steps construct the base URL to get data
baseURL= "https://graph.facebook.com/v2.5"
node = "/" + company + "/posts"
accessToken='provide access_token to get data'
parameters = "/?fields=message,created_time&access_token=%s&limit=%s" % (accessToken, numberOfPosts)

# function to process data and write JSON structure to file
def processData(data):
    finalData={}
    posts= []
    postDetails = {}
    n = len(data["data"])
    currentTimeStamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    finalData['Organization']= company
    finalData['File Generated on']= currentTimeStamp
    for i in range(0,n):
        post_message = data["data"][i]["message"]
        post_date= data["data"][i]["created_time"]
        postDetails['post'] = post_message
        postDetails['date']= post_date
        posts.append(postDetails)
    finalData['RecentPosts']=posts
    with open("ExpediaPosts.txt", "w+") as outfile:
        json.dump(finalData, outfile)

if numberOfPosts <= 10:
    url = baseURL + node + parameters
    retrievedData=getDataFromGraphAPI(url)
    processData(retrievedData)
else:
    parameter = "/?fields=message,created_time&access_token=%s&limit=%s" % (accessToken, 10)
    url = baseURL + node + parameter
    retrievedData = getDataFromGraphAPI(url)
    numberOfTimes = numberOfPosts % 10
    for i in range(0, numberOfTimes):
        next = retrievedData["paging"]["next"]
        retrievedData = getDataFromGraphAPI(next)
    processData(retrievedData)