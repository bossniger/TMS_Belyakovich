input_data = int(input())
days = input_data // (24 * 3600)
input_data %= (24 * 3600)
minutes = input_data // 60
input_data %= 60

print(f"{days} дней, {minutes} минут и {input_data} секунд")
