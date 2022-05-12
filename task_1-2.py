# калькулятор
# обернуть в try/except


while True:
    input_data_1 = input("Input first number or 'q' to out: ")
    if input_data_1 == 'q':
        break
    input_data_2 = input("Input second number or 'q' to out: ")
    if input_data_2 == 'q':
        break
    input_data_3 = input("Input operator ('+', '-', '*', '/') or 'q' to out: ")
    if input_data_3 == 'q':
        break

    # if input_data_1 == 'q' or input_data_2 == 'q' or input_data_3 == 'q':
    #     break
    elif input_data_3 == "+":
        result_data = int(input_data_1) + int(input_data_2)
        print(result_data)
        continue
    elif input_data_3 == "-":
        result_data = int(input_data_1) - int(input_data_2)
        print(result_data)
        continue
    elif input_data_3 == "*":
        result_data = input_data_1 * input_data_2
        print(result_data)
        continue
    elif input_data_3 == "/":
        try:
            result_data = input_data_1 / input_data_2
            print(result_data)
        except ZeroDivisionError:
            print("I can't divide by zero but smbd told me that it may be infinite :)")
        continue
