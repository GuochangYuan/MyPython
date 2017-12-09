import json

numbers=[2,3,5,7,11,13]

filename='numbers.json'
with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj)

with open(filename) as f_obj:
	numbers2=json.load(f_obj)

print(numbers2[2])
