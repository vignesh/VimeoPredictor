import requests
import json
import vimeo
import httplib, urllib, base64
from random import randrange
import csv

v = vimeo.VimeoClient(
    token='2c7976cf2b09e45cbe6f2fec29c8e573',
    key='94e461773b49eef4d8f9a5a7cf175a641b230826',
    secret='RTrTcAbDqvzRrwwAeThT3PR7vHjfKbtb1sN0j3c7LAFsJZYJYe0fxH2yAMj5RbXXjQsWdQM94VsfoXTy5XzZxMcIzgB1qveNs244vQH6843nfRbbH50aPWl5ZJa080wx'
    )

class Video:

    def __init__(self): #constructor
        page = randrange(1, 50)
        per_page = randrange(1, 100)
        self.parameters = {"page": page, "per_page": per_page} #parameters 
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

    def getData(self):
        response = v.get("https://api.vimeo.com/videos?", params = self.parameters, headers=self.header) #get random video
        self.views = json.loads(response.content)["data"][0]["stats"]["plays"]
        self.description =  json.loads(response.content)["data"][0]["description"]
        self.description =  self.description.strip('\n')
        self.duration = json.loads(response.content)["data"][0]["duration"]        
        self.user = json.loads(response.content)["data"][0]["user"]["name"]
        self.account = json.loads(response.content)["data"][0]["user"]["account"]
        self.followers = json.loads(response.content)["data"][0]["user"]["metadata"]["connections"]["followers"]["total"]
        self.following = json.loads(response.content)["data"][0]["user"]["metadata"]["connections"]["following"]["total"]
        self.groups = json.loads(response.content)["data"][0]["user"]["metadata"]["connections"]["groups"]["total"]
        self.likes = json.loads(response.content)["data"][0]["user"]["metadata"]["connections"]["likes"]["total"]
        self.videos = json.loads(response.content)["data"][0]["user"]["metadata"]["connections"]["videos"]["total"]
        self.shared = json.loads(response.content)["data"][0]["user"]["metadata"]["connections"]["shared"]["total"]

    def getSentiment(self):
        data = {"documents": [{"language": "en","id": "string","text": self.description}]}
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Ocp-Apim-Subscription-Key': 'f2c5cb9458b64fa5835f85b417285934'}
        url = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'
        r = requests.post(url, data = json.dumps(data), headers = headers)
        content = json.loads(r.content)
        self.score =  content['documents'][0]['score']

    def writeFile(self):
        total = ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\"%s\",%s\n" % (self.user, self.account, self.followers, self.following, self.likes, self.shared, self.videos, self.groups, self.duration, self.views, self.description, self.score))
        with open('output.csv','ab+') as f:
            #f.write("User,Account,Followers,Following,Likes,Shared,Videos,Group,Views,Duration,Description,Score")
            f.write(total.encode('utf-8'))
            f.close()

Instance = Video()
Instance.getData()
Instance.getSentiment()
Instance.writeFile()
