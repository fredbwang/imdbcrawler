import pandas as pd
from numpy import nan
import re
import math

# read data
raw_data = pd.read_csv('imdbMovies_modified.csv')
newid = []


for i in range(0, len(raw_data['imdbVotes'])):
    # print raw_data['imdbVotes'][i], i
    if type(raw_data['imdbVotes'][i]) != float or not math.isnan(raw_data['imdbVotes'][i]):
        print type(raw_data['imdbVotes'][i]), i
        newid.append(raw_data['imdbID'][i])

# print newid
output = pd.DataFrame()
output['newID'] = newid

output.to_csv('output1.csv', index=False, header=True)
