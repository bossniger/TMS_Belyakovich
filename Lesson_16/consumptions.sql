CREATE DATABASE Consumption_food;
create table Users(
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender TEXT CHECK ( gender in ('Male', 'Female') ) NOT NULL,
    -- расчет питания зависит от пола
    height DECIMAL(5, 2) NOT NULL,
    weight DECIMAL (5, 2) NOT NULL
);
CREATE TABLE Consumptions(
    id INT PRIMARY KEY ,
    user_id INT,
    date DATE NOT NULL,
    -- когда поел, наверное это важно )
    time TIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);
CREATE TABLE Products(
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    calories DECIMAL(6,2) NOT NULL,
    protein DECIMAL(6,2) NOT NULL,
    carbs DECIMAL(6,2) NOT NULL,
    fat DECIMAL(6,2) NOT NULL
-- значения белков, жиров и углеводов должны быть заполнены
);