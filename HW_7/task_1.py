# Написать программу которая получит имя и возраст пользователя,
# записывает данные в JSON, CSV, Excel
import json
import csv
import pandas as pd

users = dict()
user = dict()

user_name = str(input("Enter your name: "))
user_age = int(input("Enter your age in years: "))

user['name'] = user_name
user['age'] = user_age
users[user_name] = user

print(f'user: {user}')
print(f'users: {users}')


# JSON
with open("data_file.json", "w") as write_file:
    json.dump(users, write_file)

# CSV
keys = []
values = []
for key, value in user.items():
    keys.append(key)
    values.append(value)

csv_data = [keys, values]
csv_file = open('data_file.csv', 'w')
with csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_data)

# Excel
df = pd.DataFrame(users)
df.to_excel('./data_file.xlsx', sheet_name='users')
# df.to_excel('./data_file.xlsx', sheet_name='users', index=False)
