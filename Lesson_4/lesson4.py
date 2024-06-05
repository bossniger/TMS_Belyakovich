users = [
    {
        'name': 'victor',
        'age': 24,
        'is_working': False,
        'citizenship': ['Russian', 'England']
    },
    {
        'name': 'alice',
        'age': 16,
        'is_working': True,
        'citizenship': ['American']
    },
    {
        'name': 'bob',
        'age': 20,
        'is_working': True,
        'citizenship': ['Australian']
    }
]


# task 1.1
def print_name_and_ages(users):
    for user in users:
        print(f"Name: {user['name']}, Age: {user['age']}")


# task 1.2 and 1.2*
def print_adult_name_and_ages(users, age_check=18):
    for user in users:
        if user['age'] >= age_check:
            print(f"Name: {user['name']}, Age: {user['age']}")


# task 1.3
def print_user_citizenship(users):
    user_citizenship_dict = {}
    for user in users:
        user_citizenship_dict[user['name']] = user['citizenship']
    print(user_citizenship_dict)


# task 1.4
def add_status_to_users(users):
    for user in users:
        if(user['age'] < 18 and user['is_working']) or (user['age'] >= 18 and not user['is_working']):
            user['status'] = 'suspicious'
        else:
            user['status'] = 'not_suspicious'
        return users


def main():
    print_name_and_ages(users)
    print_adult_name_and_ages(users)
    print_user_citizenship(users)
    updated_users = add_status_to_users(users)
    print(updated_users)