import sqlite3

def create_tables():
    conn = sqlite3.connect('cassa.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS articoli (
                      id INTEGER PRIMARY KEY,
                      nome TEXT,
                      prezzo REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS vendite (
                      id INTEGER PRIMARY KEY,
                      articolo_id INTEGER,
                      quantita INTEGER,
                      data TEXT,
                      FOREIGN KEY(articolo_id) REFERENCES articoli(id))''')
    conn.commit()
    conn.close()

create_tables()
