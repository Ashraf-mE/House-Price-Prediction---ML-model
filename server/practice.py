import json 
import numpy as np 
import pandas as pd
import pickle

# arr = ['a', 'b', 'c', 'd', 'e', 'f']

# print(np.where(arr == 'a'))

with open('server/artifacts/BHP_Columns.json', 'r') as json_data:
    data = json.load(json_data)
    print(data)

locations = data['data_locations']
print(locations)

input = 'lakshminarayana pura'

location_index = locations.index(input)
print(location_index)


model = pickle.load(open('./server/artifacts/BHP.pkl', 'rb'))

model.predict(input, )






