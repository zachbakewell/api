import requests
import json

url = 'https://api.fbi.gov/wanted/v1/list'
r = requests.get(url)

if r.status_code == requests.codes.ok:

    outfile = open('fbi.json','w')\
    
    r_dictionary = r.json()

    json.dump(r_dictionary, outfile, indent=4)

    most_wanted_list = r_dictionary['items']

    for x in most_wanted_list:
        if x['subjects'] == ['Vicap Missing Persons'] and isinstance(int(x['age_min'])):
            if x['age_min'] < 25:
                name = x['title']
                url = x['files'][0]['url']
                sex = x['sex']
                age = x['age_min']
                eyes = x['eyes']
                hair = x['hair']
                weight = x['weight_min']

                print(f'Name: {name}')
                print(f'FBI Direct Link: {url}')
                print(f'Gender: {sex}')
                print(f'Age: {age}')
                print(f'Eye Color: {eyes}')
                print(f'Hair Color: {hair}')
                print(f'Weight: {weight}')
                print()
                print()