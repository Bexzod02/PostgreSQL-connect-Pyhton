import psycopg2

host = 'localhost'
username = "postgres"
password = "1234"
db_name = 'shop'
port = 5432

conn = None
curr = None
try:
    # connect to exist database
    conn = psycopg2.connect(
        host=host,
        user=username,
        password=password,
        dbname =db_name,
        port=port
    )
    curr = conn.cursor()
    conn.autocommit=True
    # the cursor for performing database operaions
    # cursor = connection.cursor()
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")


    #CREATE TABLE

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         "CREATE TABLE table_name(columns)"
    #     )

        # connection.commit
    #     print(f"Table created succesfully")

    #INSERT data into a table

    # with conn.cursor() as cursor:
    #     cursor.execute(
    #         """ INSERT INTO category(id, title)values(2, 'hello'); """
    #     )
    #     print("[INFO] Data was successfully inserted")
        
    # get data from a table
    with conn.cursor() as cursor:
        cursor.execute(
            """ SELECT * from category; """
        )
        for x in cursor:
            print(x)
        # print(cursor.fetchone())

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if curr:
        curr.close()
    if conn:
        # cursor.close()
        conn.close()
        print("[INFO] PostgreSQL connection closed")





