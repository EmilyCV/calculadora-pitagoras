import sqlite3

# Conectando
conn = sqlite3.connect('database.db', check_same_thread=False)

# Definindo um cursor
cursor = conn.cursor()


def create_db():
    cursor.execute(f"""
    CREATE TABLE user (
    email TEXT NOT NULL
               PRIMARY KEY,
    nome  TEXT NOT NULL
);
CREATE TABLE catetos (
    id              INTEGER NOT NULL
                            PRIMARY KEY AUTOINCREMENT,
    catetoOposto    NUMERIC NOT NULL,
    catetoAdjacente NUMERIC NOT NULL,
    resultado       NUMERIC NOT NULL,
    email           STRING  NOT NULL,
    FOREIGN KEY (
        email
    )
    REFERENCES user (email) 
);  
    """)


def create_user(email, name):
    with sqlite3.connect('database.db') as con:
        cursor.execute(
            "INSERT INTO user (email,nome) VALUES (?,?)", (email, name))
        cursor.execute('COMMIT')
        msg = "Done"
        conn.close()


# Fechando conexão
# conn.close()
