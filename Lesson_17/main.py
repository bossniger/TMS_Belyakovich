import psycopg2


class Database:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(dbname=dbname,
                                     user=user,
                                     password=password,
                                     host=host,
                                     port=port)
        self.cur = self.conn.cursor()

    def create_product_table(self):
        self.cur.execute("""
            CREATE TABLE products(
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                proteins FLOAT,
                fats FLOAT,
                carbohydrates FLOAT
                )
            """)
        self.conn.commit()

    def add_product(self, name, proteins, fats, carbohydrates):
        self.cur.execute("""
            INSERT INTO products (name, proteins, fats, carbohydrates) VALUES (%s, %s, %s, %s)
            """, (name, proteins, fats, carbohydrates))
        self.conn.commit()

    def create_user_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INTEGER,
                gender VARCHAR(10)
            )
        """)
        self.conn.commit()

    def add_user(self, name, age, gender):
        self.cur.execute("""
            INSERT INTO users (name, age, gender) VALUES (%s, %s, %s)
        """, (name, age, gender))
        self.conn.commit()

    def create_meal_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS meals(
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                product_id INTEGER REFERENCES products(id),
                meal_time TIMESTAMP
            )
        """)
        self.conn.commit()

    def add_meal(self, user_id, product_id, meal_time):
        self.cur.execute("""
            INSERT INTO meals (user_id, product_id, meal_time) VALUES (%s, %s, %s)
        """, (user_id, product_id, meal_time))
        self.conn.commit()

    def close_connection(self):
        self.cur.close()
        self.conn.close()


# создаем таблицы
db = Database('lesson_17', 'postgres', '123', '127.0.0.1', '5432')
db.create_product_table()
db.create_user_table()
db.create_meal_table()
# делаем записи в таблицу
db.add_product("Apple", 0.5, 0.2, 10.3)
db.add_user("Alice", 30, "Female")
db.add_meal(1, 1, "2024-07-07 08:00:00")
db.close_connection()
