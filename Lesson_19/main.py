import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Получаем айдишник последнего добавленного продукта в список
def get_last_id():
    with open('products.json') as file:
        data = json.load(file)
        last_id = max([event['id'] for event in data['products']])
    return last_id


# Добавляем новый продукт в список
def add_product_to_json(new_product):
    with open('products.json', 'r') as file:
        data = json.load(file)
    data['products'].append(new_product)
    with open('products.json', 'w') as file:
        json.dump(data, file, indent=4)


# Добавление продукта в список потребленных продуктов
def add_ate_product(product_id):
    with open('products.json', 'r') as file:
        products_list = json.load(file)

    ate_product = None
    for product in products_list['products']:
        if int(product['id']) == int(product_id):
            ate_product = product

    if ate_product:
        with open('eated_products.json', 'r') as file:
            ate_products_list = json.load(file)
        ate_products_list['ate_products'].append(ate_product)
        with open('eated_products.json', 'w') as file:
            json.dump(ate_products_list, file, indent=4)
    else:
        print("Product is not found")


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


@app.route('/products/<int:product_id>')
def update_ate_products(product_id):
    add_ate_product(product_id)
    return render_template('index.html')


@app.route('/myfood')
def show_my_food():
    with open('eated_products.json', 'r') as file:
        calories_sum = 0
        data = json.load(file)
        ate_products = data['ate_products']
        for d in data['ate_products']:
            calories_sum += d['calories']
    return render_template('my_food.html', ate_products=ate_products, calories_sum=calories_sum)


if __name__ == "__main__":
    app.run(debug=True)
