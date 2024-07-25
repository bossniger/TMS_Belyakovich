import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def get_last_id():
    with open('products.json') as file:
        data = json.load(file)
        last_id = max([event['id'] for event in data['products']])
    return last_id


def add_product_to_json(new_product):
    with open('products.json', 'r') as file:
        data = json.load(file)
    data['products'].append(new_product)
    with open('products.json', 'w') as file:
        json.dump(data, file, indent=4)


@app.route('/', methods=['GET'])
def draw_main_page():
    return render_template('index.html')


@app.route('/products', methods=['GET', 'POST'])
def show_products():
    with open('products.json', 'r') as file:
        data = json.load(file)
        products = data['products']
    return render_template('products.html', products=products)


@app.route('/new_product', methods=['GET', 'POST'])
def create_product():
    if request.method == "POST":
        name = request.form['name']
        protein = float(request.form['protein'])
        fats = float(request.form['fats'])
        carbohydrates = float(request.form['carbohydrates'])
        calories = float(request.form['calories'])
        new_product = {
            'id': (get_last_id() + 1),
            'name': name,
            'protein': protein,
            'fats': fats,
            'carbohydrates': carbohydrates,
            'calories': calories
        }
        add_product_to_json(new_product)
        return redirect(url_for('show_products'))
    return render_template('new_product.html')


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