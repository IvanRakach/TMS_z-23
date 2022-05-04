# Написать программу, которая посчитает и выведет результат выражения
# Проверить, является ли результат выражения типом данных int

users_input_data = ((2 ** 5) * 2 - 16 * 2) / (8 ** 8)
print(f"Result: {users_input_data}")

print(type(users_input_data))

if type(users_input_data) is int:
    print("Data type is 'int'")
else:
    print("Data type is NOT 'int'.")
