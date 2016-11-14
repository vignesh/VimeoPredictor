class Predict:

	def __init__(self): 
		self.duration = raw_input("How many seoncds is your video?")
		self.followers = raw_input("How many users do you have?")
		self.level = raw_input("What is your Vimeo subscription level?")
		self.description = raw_input("What is the description of your video?")

	#def getUserInfo(self):

	def getSentiment(self):
        data = {"documents": [{"language": "en","id": "string","text": self.description}]}
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Ocp-Apim-Subscription-Key': 'f2c5cb9458b64fa5835f85b417285934'}
        url = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'
        r = requests.post(url, data = json.dumps(data), headers = headers)
        content = json.loads(r.content)
        self.score =  content['documents'][0]['score']

    def calculateViews(self):
        self.views =  self.score*0.25 + self.duration*0.25 + self.followers*0.25 + self.level*0.25
        print "Your video is predicted to have %s views" % (self.views)

Video = Predict()
Video.getSentiment()
Video.calculateViews()