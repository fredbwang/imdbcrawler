import pandas as pd
from pandas import DataFrame
import re

df = pd.read_csv('IMDBfinal16000xue.csv')

# IMDBRate actually is IMDBid
length = len(df['IMDBRate'])
IDdict = {}

for i in range(0, length):
    pattern = re.compile(r'[tt]+\d+[/]')
    match = pattern.findall(df['IMDBRate'][i])
    for j in range(0, len(match)):
        # IDindex = j * 19 + 10
        # movieID = int(df['IMDBRate'][i][IDindex:IDindex + 7])
        movieID = int(match[j][2:9])
        if movieID in IDdict.keys():
            IDdict[movieID] += 1
        else:
            IDdict[movieID] = 1

output = DataFrame()

output['ID'] = IDdict.keys()
output['number of comments'] = IDdict.values()
output.to_csv('movie_popular_index.csv', index=False, header=True)

'''
count = 0
ratesNumber = 0
threshold = 10
for i in IDdict:
    # get the number of popular movies rated by more than x users
    if IDdict[i] > threshold:
        count += 1
        ratesNumber += IDdict[i]

print 'number of rates', ratesNumber
print 'total number of movies:', len(IDdict)
print 'number of poplar movies', count


# get the sum of a user's all rated movies' total rates
sumlist = []
for i in range(0, length):
    # total rates of this user
    sum = 0
    for j in range(0, len(df['IMDBRate'][i]) / 19):
        IDindex = j * 19 + 10
        movieID = int(df['IMDBRate'][i][IDindex:IDindex + 7])
        sum += IDdict[movieID]
    sumlist.append(sum)

print sumlist
'''