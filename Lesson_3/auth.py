with open("db.txt", "r") as file:
    lines = file.readlines()
users = []
current_dict = {}
for line in lines:
    if ":" in line:
        key, value = line.strip().split(":")
        if key in current_dict:
            users.append(current_dict)
            current_dict = {}
            current_dict[key] = value
        else:
            current_dict[key] = value
    elif len(line.strip()) == 0:
        print('XD')
users.append(current_dict)


def save_users():
    with open('db.txt', 'w') as file:
        for user in users:
            for key, val in user.items():
                file.write('{}:{}\n'.format(key, val))


def register():
    login = input('Введите ваш ник: ')
    password = input('Введите ваш пароль')
    age = int(input('Введите ваш возраст'))
    users.append({'login': login, "password": password, 'age': age})
    save_users()
    print('Регистрация прошла успешно!')


def authenticate():
    login = str(input('Введите ваш ник: '))
    password = input('Введите ваш пароль')
    for user in users:
        if user['login'] == login and user['password'] == password:
            return user
    return None


while True:
    print('Выберите действие:')
    print('1. Зарегистрироваться')
    print('2. Аутентифицироваться')
    print('3. Выход')
    choice = input()

    if choice == '1':
        register()
    elif choice == '2':
        user = authenticate()
        if user:
            print(f"Добро пожаловать, {user['login']}!")
            while True:
                print('Выберите действие:')
                print('1. Поменять возраст')
                print('2. Разлогиниться')
                inner_choice = input()
                if inner_choice == '1':
                    new_age = int(input('Введите ваш новый возраст: '))
                    user['age'] = new_age
                    save_users()
                    print('Возраст успешно изменен.')
                elif inner_choice == '2':
                    break
                else:
                    print('Неверное действие. Попробуйте снова.')
        else:
            print('Неверный ник или пароль. Попробуйте снова.')
    elif choice == '3':
        break
    else:
        print('Неверное действие. Попробуйте снова.')