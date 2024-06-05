from getters import get_email, get_password
users = [
    {
        'email': 'some@mail.ru',
        'password': '123pass'
    },
    {
        'email': 'second@mail.ru',
        'password': '213pass'
    },
    {
        'email': 'third@mail.ru',
        'password': '321pass'
    }
]


def check_data(email, password):
    for user in users:
        if user['email'] == email and user['password'] == password:
            return email
    return 'Ошибка: неверный email или пароль'