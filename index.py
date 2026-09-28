import psycopg2

conection = psycopg2.connect(
    host = "localhost",
    port = "5432",
    database = "book_store",
    user = "postgres",
    password = "12345678"
)

print("connection successful")

curso = conection.cursor()

curso.execute(
    "SELECT * from users;"
)

one_row = cursor.fetchone()
print(one_row)

next = cursor.fetchmany(2)
print(next)

one = cursor.fetchone()
print(one)
