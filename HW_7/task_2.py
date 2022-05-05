# Сделать программу для записи и чтения из файла .txt

user_name = str(input("Enter your name: "))
user_age = int(input("Enter your age in years: "))

users_list = [user_name, user_age]
print(f'user: {users_list}')

# write
f = open("data_file.txt", 'w')
f.writelines("%s\n" % word for word in users_list)
f.close()

# read
open("data_file.txt").read()
print(open("data_file.txt").read())
