# Сделать программу, в которой нужно угадать число

task_number = 7
user_input_number = 0

while task_number != user_input_number:
    user_input_number = float(input('Enter your number: '))
    if user_input_number == task_number:
        print("You are win!!!!!")
    elif (user_input_number/task_number) <= 0.15:
        print('Very cold! Try again!')
    elif 0.15 < (user_input_number / task_number) <= 0.3:
        print('Cold! Try again!')
    elif 0.3 < (user_input_number / task_number) <= 0.45:
        print('Warm! Try again!')
    elif 0.45 < (user_input_number / task_number) <= 0.6:
        print('Warmer!!! Try again!')
    elif 0.6 < (user_input_number / task_number) <= 0.75:
        print('You are more and more closer!!! Try again!')
    elif 0.75 < (user_input_number / task_number) <= 0.9:
        print('You are sooooo close!!! Try again!')
    elif (user_input_number/task_number) > 0.9 and (user_input_number/task_number) != 1:
        print('You are sooooo close!!! Try again!')

