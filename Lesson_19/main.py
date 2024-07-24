import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def draw_main_page():
    return render_template('index.html')


@app.route('/products', methods=['GET', 'POST'])
def show_products():
    with open('products.json', 'r') as file:
        data = json.load(file)
        products = data['products']
    return render_template('products.html', products=products)

if __name__ == "__main__":
    app.run(debug=True)
# # Открываем JSON файл для чтения
# with open('products.json', 'r') as file:
#     data = json.load(file)
#
# new_product = {
#     'name':"igor",
#     'age':3,
#     'email':"3@gmail.com"
# }
# data['products'].append(new_product)
#
# # Записываем обновленные данные в JSON файл
# with open('products.json', 'w') as file:
#     json.dump(data, file, indent=4)
#
# print("Данные успешно добавлены в JSON файл.")