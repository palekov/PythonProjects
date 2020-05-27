def iterate_by_passwords_then_by_logins(login_generator, password_generator, query):
    """

    :param login_generator:
    :param password_generator:
    :param query:
    """
    password_state = None
    while True:
        password, password_state = password_generator(password_state)

        login_state = None
        while True:
            login, login_state = login_generator(login_state)
            if query(login, password):
                print('Success', login, password)
            if login_state is None:
                break

        if password_state is None:
            break


def iterate_by_logins_then_by_limited_passwords(login_generator, password_generator, query):
    limit = 100000
    login_state = None
    while True:
        login, login_state = login_generator(login_state)
        password, password_state = password_generator(None)
        for i in range(limit):
            if query(login, password):
                print('Success', login, password)
                break
            password, password_state = password_generator(password_state)
            if password_state is None:
                break

        if login_state is None:
            break
