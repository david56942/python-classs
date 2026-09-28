import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    port = "5432",
    database = "class_book_store_db",
    user = "postgres",
    password = "12345678"
)
print("conected")
cursor = connection.cursor()

name = "daniel"
email = "daniel@gmail.com"
cursor.execute(
    "INSERT INTO users (name, email) VALUES (%s, %s)",
    (name,email)
)
connection.commit()
connection.close()
