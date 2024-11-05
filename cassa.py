import sqlite3

def aggiungi_articolo(nome, prezzo):
    conn = sqlite3.connect('cassa.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO articoli (nome, prezzo) VALUES (?, ?)", (nome, prezzo))
    conn.commit()
    conn.close()
def registra_vendita(articolo_id, quantita):
    conn = sqlite3.connect('cassa.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vendite (articolo_id, quantita, data) VALUES (?, ?, DATE('now'))", 
                   (articolo_id, quantita))
    conn.commit()
    conn.close()
