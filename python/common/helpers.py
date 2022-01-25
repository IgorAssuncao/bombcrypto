def get_user_int_input(message: str) -> int:
    user_input = input(message)
    user_input_as_int = 0
    is_int = False
    while not is_int:
        try:
            user_input_as_int = int(user_input)
            is_int = True
        except ValueError:
            print('Please, it must be an integer. Try again.')
            user_input = input(message)

    return user_input_as_int

