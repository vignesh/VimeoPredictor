import pandas as pd
import numpy as np
from csv import reader
from matplotlib import pyplot

"""COLUMN_SEPARATOR = '  '
paramnames= ["Views", "Score", "Followers", "Duration", "Level"]
#video_data = pd.DataFrame.from_csv('cleandata.csv', sep=COLUMN_SEPARATOR, header=1)
video_data = pd.read_csv('cleandata.csv', names=paramnames)
np.polyfit(video_data['Views'], video_data['Score'], 1)
#print video_data[:10][2:]

#engine_doc = engine : {'c', 'python'}"""

""""SENTIMENT_INDEX = 1
VIEWS_INDEX = 2
x = video_data[SENTIMENT_INDEX]
y = video_data[VIEWS_INDEX]
regression = np.polyfit(x, y, 1)"""

with open('cleandata.csv', 'r') as f:
    data = list(reader(f))

views = [i[0] for i in data]
score = [i[1] for i in data]
followers = [i[2] for i in data]
duration = [i[3] for i in data]
level = [i[4] for i in data]
pyplot.plot(views, level)
pyplot.show()


"""AVG 256.8857143, STD 430.5510976, basic- 1
4228, 1, business
268.4683544, 376.996438, plus- 2
529.3195876, 529.3195876, pro- 3"""

#Views, Score, Followers, Duration, Level