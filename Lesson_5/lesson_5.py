from random import randint


def create_user_numbers_list(user_input):
    user_numbers = []
    for number in user_input.split():
        user_numbers.append(int(number))
    return user_numbers


def check_numbers(guessed_numbers, user_numbers):
    correct_numbers = 0
    for i in range(3):
        if user_numbers[i] in guessed_numbers:
            correct_numbers += 1
    return correct_numbers


def guess_numbers(min_num, max_num):
    numbers = []
    while len(numbers) < 3:
        num = randint(min_num, max_num)
        if num not in numbers:
            numbers.append(num)
    return numbers


def main():
    min_num = int(input("Введите минимальное число в диапазоне от 5 до 30: "))
    max_num = int(input("Введите максимальное число в диапазоне от 5 до 30: "))

    if min_num < 5 or max_num > 30:
        print("Неверный диапазон чисел. Попробуйте еще раз")
        return

    guessed_numbers = guess_numbers(min_num, max_num)

    while True:
        user_input = input("Введите три числа через пробел или введите exit для выхода из программы: ")
        if user_input.lower() == "exit":
            print("чао!")
            break

        user_numbers = create_user_numbers_list(user_input)
        if len(user_numbers) != 3:
            print("Неверный формат ввода. Попробуй еще раз! ")
        correct_numbers = check_numbers(guessed_numbers, user_numbers)
        if correct_numbers == 3:
            print("You win!")
            break
        else:
            print("Try again")


main()