import requests
import pandas as p

url = 'https://randomuser.me/api/?results=100&gender=male'

#send a get request
response = requests.get(url)
names = response.json()

filter = p.json_normalize(names['results'])
male_users = filter[filter['gender']=='male'].reset_index(drop=True)

top_male_users = []
for i, row in male_users.head(100).iterrows():
    names = f"{row['name.first']} {row['name.last']}"
    top_male_users.append(f"{i+1}. {names}")

print("Here are the Top 100 users: \n")
for user in top_male_users:
    print(user)

