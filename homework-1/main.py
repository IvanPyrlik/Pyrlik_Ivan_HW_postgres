"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

with psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="ivan9675"
) as conn:
    with conn.cursor() as cur:
        with open('north_data/employees_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # пропуск хедера
            for row in reader:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                            (row[0], row[1], row[2], row[3], row[4], row[5]))
                cur.execute("SELECT * FROM employees")

        with open('north_data/customers_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # пропуск хедера
            for row in reader:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                            (row[0], row[1], row[2]))
                cur.execute("SELECT * FROM customers")

        with open('north_data/orders_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # пропуск хедера
            for row in reader:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                            (row[0], row[1], row[2], row[3], row[4]))
                cur.execute("SELECT * FROM orders")

conn.close()
