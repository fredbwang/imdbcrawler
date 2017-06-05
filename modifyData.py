import pandas as pd
import re
import math
import numpy as np


def getBoxOfficeLevel(i):
    if type(i) is np.float64 and not math.isnan(i):
        return math.log(i, 10)
    else:
        return float(6) + np.random.randn()


def switchCountry(i):
    if i == 'USA':
        return 0
    elif i == 'Italy' or i == 'France' or i == 'Germany' or i == 'Spain' or i == 'UK' or i == 'Russia':
        return 1
    elif i == 'China' or 'Hong Kong' or 'Taiwan':
        return 2
    elif i == 'Japan' or 'South Korea':
        return 3
    elif i == 'India':
        return 4
    else:
        return 5


def getCountry(country):
    # no value
    if not type(country) is str:
        return 5
    else:
        # get first country
        pattern = re.compile(r'.+[,]')
        match = pattern.search(country)
        if match:
            i = str(country[match.start(0):match.end(0) - 1])
            #print i
            return switchCountry(i)
        else:
            # there is only one country so there is no ','
            return switchCountry(country)

# calculate award score of each movie
def getAwardScore(OscarWins, OscarNoms, GoldenWins, GoldenNoms, OtherWins, OtherNoms, i):
    # print type(OscarWins), i
    if type(OscarWins) is str:
        OscarWins = int(OscarWins)
    elif math.isnan(OscarWins):
        OscarWins = 0

    if type(OscarNoms) is str:
        OscarNoms = int(OscarNoms)
    elif math.isnan(OscarNoms):
        OscarNoms = 0

    if type(GoldenWins) is str:
        GoldenWins = int(GoldenWins)
    elif math.isnan(GoldenWins):
        GoldenWins = 0

    if type(GoldenNoms) is str:
        GoldenNoms = int(GoldenNoms)
    elif math.isnan(GoldenNoms):
        GoldenNoms = 0

    if type(OtherWins) is str:
        OtherWins = int(OtherWins)
    elif math.isnan(OtherWins):
        OtherWins = 0

    if type(OtherNoms) is str:
        OtherNoms = int(OtherNoms)
    elif math.isnan(OtherNoms):
        OtherNoms = 0

    return 5 * float(OscarWins) + 2 * float(OscarNoms) + 2 * float(GoldenWins) \
            + 1 * float(GoldenNoms) + 0.3 * float(OtherWins) + 0.1 * float(OtherNoms)

# classify quality of each movie according to awards
def getAwardLevel(score):
    return math.log(score + 1, 2)
'''
    i = score
    if i == 0:
        return 0
    elif 0 < i <= 5:
        return 1
    elif 5 < i <= 20:
        return 2
    elif 20 < i <= 50:
        return 3
    elif 50 < i <= 100:
        return 4
    elif 100 < i:
        return 5
    else:
        return 
'''


def getRated(i):
    if i == 'PG-13':
        return 0
    elif i == 'PG':
        return 1
    elif i == 'TV-14':
        return 2
    elif i == 'TV-MA':
        return 3
    elif i == 'R':
        return 4
    else:
        return 0


def getRuntime(text):
    if type(text) == str:
        pattern = re.compile(r'\d+\s+[min]')
        match = pattern.search(text)
        if match:
            time = int(text[match.start(0):match.end(0) - 1])
            if 0 < time <= 90:
                return 0.1
            elif 90 < time <= 110:
                return 0.2
            elif 110 < time <= 130:
                return 0.3
            elif 130 < time <= 150:
                return 0.4
            elif 150 < time:
                return 0.5
            else:
                return 0
    else:
        return 0.2


def getGenre(text, genre):
    # print genre,
    if type(text) is str:
        pattern1 = re.compile(r'\w+[,]')
        pattern2 = re.compile(r'\s\w+')
        prime = pattern1.findall(text)
        secondary = pattern2.findall(text)
        secondary1 = []
        prime1 = []

        if prime:
            prime1.append(prime[0][:-1])
            if genre in prime1:
                return 3
            elif secondary:
                for i in range(0, len(secondary)):
                    secondary1.append(secondary[i][1:])
                if genre in secondary1:
                    return 1
                else:
                    return 0
        else:
            if genre == text:
                return 3
            else:
                return 0
    else:
        return 0


def getProducer(text):
    if type(text) is str:
        if text is 'Walt Disney Pictures':
            return 5
        elif text=='20th Century Fox' or text=='Universal Pictures' or text=='Warner Bros. Pictures' or text=='Columbia Pictures':
            return 4
        else:
            return 3
    else:
        return 2


def getimdbVotes(votes):
    # print type(votes)
    if type(votes) is np.float64 and not math.isnan(votes):
        return math.log(votes, 10)
    else:
        return float(2) + 0.5 * np.random.randn()


def getimdbRatings(ratings):
    if type(ratings) is str:
        pattern = re.compile(r'\d+[.]+\d')
        match = pattern.findall(ratings)
        if match:
            return float(match[0])
        else:
            return float(6)
    else:
        return float(6) + np.random.randn()


def getRotten(ratings):
    if type(ratings) is np.float64 and not math.isnan(ratings):
        return float(ratings * 10)
    else:
        return float(6.2) + np.random.randn()


def getMeta(ratings):
    if type(ratings) is np.float64 and not math.isnan(ratings):
        return float(ratings) / 10
    else:
        return float(5) + np.random.randn()


def getRealsed(dates):
    if math.isnan(dates):
        return np.random.randn()
    else:
        if float(dates) / 40000:  # movie before year 2000
            return float(dates) / 43000
        else:  # movie after year 2000 we get its release season
            return float(dates) % 365 / 365

# read data
raw_data = pd.read_csv('imdbMovies_simple.csv')

# this part has a problem, when you apply large data like 2000 tuples then the calculating is not working,
# the AwardScore will all be zero
awardScore = []
awardLevel = []
rated = []
runtime = []
imdbvotes = []
country = []
boxLevel = []
imdbratings = []
rotten = []
meta = []
released = []
producer = []
genre = []
dict_genre = {'Drama': [], 'Action': [], 'Animation': [], 'Sci-Fi': [], 'Horror': [], 'Comedy': [], 'Crime': []}

for i in range(0, len(raw_data['imdbID'])):
    print i
    awardScore.append(getAwardScore(raw_data['Oscar wins'][i], raw_data['Oscar nominations'][i], raw_data['Golden Globe wins'][i], \
                                    raw_data['Golden Globe nominations'][i], raw_data['other wins'][i], raw_data['other nominations'][i], i))
    awardLevel.append(getAwardLevel(awardScore[i]))
    rated.append(getRated(raw_data['Rated'][i]))
    runtime.append(getRuntime(raw_data['Runtime'][i]))
    imdbvotes.append(getimdbVotes(raw_data['imdbVotes'][i]))
    country.append(getCountry(raw_data['Country'][i]))
    boxLevel.append(getBoxOfficeLevel(raw_data['BoxOffice'][i]))
    imdbratings.append(getimdbRatings(raw_data['imdbRating'][i]))
    rotten.append(getRotten(raw_data['Rotten Tomatoes'][i]))
    meta.append(getMeta(raw_data['Metascore'][i]))
    released.append(getRealsed(raw_data['Released'][i]))
    producer.append(getProducer(raw_data['Production'][i]))
    for key in dict_genre:
        dict_genre[key].append(getGenre(raw_data['Genre'][i], key))

# delete useless keys
del raw_data['Oscar wins'], raw_data['Oscar nominations'], raw_data['Golden Globe wins'],
del raw_data['Golden Globe nominations'], raw_data['other wins'], raw_data['other nominations']
del raw_data['Runtime'], raw_data['Rated'], raw_data['Awards'], raw_data['imdbVotes'], raw_data['Genre']


# write data
output = raw_data
output['BoxOffice'] = (boxLevel - np.min(boxLevel)) / (np.max(boxLevel) - np.min(boxLevel))
output['Country'] = (country - np.min(country)) / (np.max(country) - np.min(country))
output['AwardLevel'] = (awardLevel - np.min(awardLevel)) / (np.max(awardLevel) - np.min(awardLevel))
output['RatedLevel'] = (rated - np.min(rated)) / (np.max(rated) - np.min(rated))
output['RuntimeLevel'] = (runtime - np.min(runtime)) / (np.max(runtime) - np.min(runtime))
output['VotesLevel'] = (imdbvotes - np.min(imdbvotes)) / (np.max(imdbvotes) - np.min(imdbvotes))
output['imdbRating'] = (imdbratings - np.min(imdbratings)) / (np.max(imdbratings) - np.min(imdbratings))
output['Rotten Tomatoes'] = (rotten - np.min(rotten)) / (np.max(rotten) - np.min(rotten))
output['Metascore'] = (meta - np.min(meta)) / (np.max(meta) - np.min(meta))
output['Released'] = released
output['Production'] = (producer - np.min(producer)) / (np.max(producer) - np.min(producer))
for key in dict_genre:
    output[key] = dict_genre[key]

output.to_csv('output1.csv', index=False, header=True)
