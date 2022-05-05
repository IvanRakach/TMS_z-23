def decorator_function(func):
    def inner_func(*args):
        """
        Starting transformation of our stand-alone function:
        1. Checking start/finish process;
        2. making html tegs;
        3. printing arguments of our stand-alone function;
        4. transforming arguments of our stand-alone function.
        """

        print('Start decorator...')
        print('<table>')
        print('<td>')
        print('<tr>')

        print(f"'test_func' parametr: {int(*args)}")
        print(f"'test_func' list: {func(args)}")

        for el in args:
            print(f"Increasing 'test_func' parametr: {el * 2}")
        print(f"Increasing 'test_func' parametr: {int(*args) * 2}")

        add_list = []
        for i in func(args):
            add_list.append(i)
            if i >= 5:
                add_list.append(i * 1000)
        print(f"Transform input parameters: {add_list}")

        print('</tr>')
        print('</td>')
        print('</table>')
        print('Finish decorator...')
    return inner_func


@decorator_function
def test_func(number: int) -> list:
    """test_func is generating list of even numbers"""
    return [number for number in range(0, 10) if number % 2 == 0]
    # print([numb for numb in range(0, 10) if numb % 2 == 0])


test_func(10)
