from flask import Flask, render_template, request
from sqlalchemy import create_engine, Column, Integer, String
import psycopg2
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine("postgresql+psycopg2://postgres:123@localhost/cars_db")

cars = Flask(__name__)
cars.debug = True


class Base(DeclarativeBase):
    pass


class Car(Base):
    __tablename__ = 'cars'

    id = Column('id', Integer(), primary_key=True, index=True)
    brand = Column('brand', String(255), nullable=False)
    model = Column('model', String(255), nullable=False)
    serial_number = Column('serial_number', String(20), nullable=False)


@cars.route('/')
def main_page():
    with Session(autoflush=False, bind=engine) as db:
        cars = db.query(Car).all()
    return render_template('index.html', cars=cars)


@cars.route('/add_car', methods = ['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        serial_number = request.form['serial_number']
        car = Car(brand=brand, model=model, serial_number=serial_number)
        with Session(autoflush=False, bind=engine) as db:
            db.add(car)
            db.commit()
        return "Car added successfully"
    return render_template('add_car.html')
# Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    cars.run(debug=True)




