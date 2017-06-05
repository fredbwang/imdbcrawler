import pandas as pd
import re
from knn import *
import math
import numpy as np

user_data = pd.read_csv('bowang(3).csv')

movielist_dict = {}
for i in range(0, len(user_data['username'])):
    username = user_data['username'][i]
    movielist = user_data['movielist'][i]
    # print type(movielist), movielist
    pattern = re.compile(r'[t]+\d+')
    match = pattern.findall(user_data['movielist'][i])
    movielist_dict[username] = match

'''
for key in movielist_dict:
    # print len(movielist_dict[key])
    for i in range(0, len(movielist_dict[key]) / 2):
        print movielist_dict[key][i],
'''
# this file is generated from modifyData
movie_data = pd.read_csv('output1.csv')

accuracy = []
len1 = []

for name in user_data['username']:
    count = 0

    # get the list of movie to be test
    test_movie_id = []
    for i in range(len(movielist_dict[name]) / 2, len(movielist_dict[name])):
        test_movie_id.append(movielist_dict[name][i])

    # for user_movie in movielist_dict[name]:
    for i in range(0, len(movielist_dict[name]) / 2):
        # print i, len(movielist_dict[name])
        imdbIDlist = list(movie_data['imdbID'])
        tuple = {}
        index = imdbIDlist.index(movielist_dict[name][i])

        # find the corresponding tuple of user_movie
        for attribute in movie_data:
            # print movie_data[attribute][index]
            tuple[attribute] = movie_data[attribute][index]
        # tuple.pop('imdbID')

        # calculate this tuple's nearest neighbor in movie_data
        (minimum, index) = getminDistance(movie_data, tuple, 0)

        # find movie id of this index
        movie_id = movie_data['imdbID'][index]
        if movie_id in test_movie_id:
            count += 1
            # print count,

    acc = float(count) / (float(len(movielist_dict[name])) / 2)
    print (acc, len(movielist_dict[name]))
    accuracy.append(acc)
    len1.append(len(movielist_dict[name]))


acc_final = float(np.sum(accuracy)) / float(len(accuracy))

output = pd.DataFrame()
output['accuracy'] = accuracy
output['len'] = len1

output.to_csv('knn_result.csv', index=False, header=True)


