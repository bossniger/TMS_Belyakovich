from getters import get_email, get_password
from validators import check_data


def main():
    while True:
        email = get_email()
        if email == 'exit':
            print('Чао!')
            break
        password = get_password()
        result = check_data(email, password)
        print(result)

main()