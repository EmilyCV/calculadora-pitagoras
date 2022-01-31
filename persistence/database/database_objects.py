import sqlite3

# Conectando
conn = sqlite3.connect('database.db',check_same_thread=False)

# Definindo um cursor
cursor = conn.cursor()

def create_db():
    cursor.execute(f"""
    CREATE TABLE user (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL);   
    """)

def create_user(name):
    with sqlite3.connect('database.db') as con:
        cursor.execute("INSERT INTO user (nome) VALUES (?)",(name,))
        cursor.execute('COMMIT')
        msg = "Done"
        conn.close()


# Fechando conexão
# conn.close()