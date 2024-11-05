import tkinter as tk
from tkinter import messagebox
from cassa import aggiungi_articolo, registra_vendita, mostra_articoli, calcola_totale, stampa_ricevuta, registra_vendita_dettagliata, genera_report_vendite

# Funzione per aggiungere un articolo
def aggiungi():
    nome = nome_entry.get()
    try:
        prezzo = float(prezzo_entry.get())
        aggiungi_articolo(nome, prezzo)
        messagebox.showinfo("Info", f"Articolo '{nome}' aggiunto con successo!")
        nome_entry.delete(0, tk.END)
        prezzo_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Errore", "Il prezzo deve essere un numero.")

# Funzione per visualizzare tutti gli articoli disponibili
def mostra_tutti_gli_articoli():
    articoli = mostra_articoli()
    articolo_text.delete(1.0, tk.END)
    for articolo in articoli:
        articolo_text.insert(tk.END, f"ID: {articolo[0]}, Nome: {articolo[1]}, Prezzo: €{articolo[2]}\n")

# Funzione per registrare una vendita
def registra():
    try:
        articolo_id = int(id_entry.get())
        quantita = int(quantita_entry.get())
        registra_vendita_dettagliata([{"id": articolo_id, "quantita": quantita}])
        messagebox.showinfo("Info", f"Vendita dell'articolo ID {articolo_id} registrata!")
        id_entry.delete(0, tk.END)
        quantita_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Errore", "ID e quantità devono essere numeri.")

# Funzione per calcolare il totale della vendita
def calcola_totale_vendita():
    try:
        articolo_id = int(id_entry.get())
        quantita = int(quantita_entry.get())
        carrello = [{'id': articolo_id, 'quantita': quantita}]
        totale = calcola_totale(carrello)
        messagebox.showinfo("Totale Vendita", f"Totale: €{totale}")
    except ValueError:
        messagebox.showerror("Errore", "ID e quantità devono essere numeri.")

# Funzione per generare e mostrare il report delle vendite
def mostra_report_vendite():
    report = genera_report_vendite()
    report_text.delete(1.0, tk.END)
    for vendita in report:
        report_text.insert(tk.END, f"Articolo: {vendita[0]}, Quantità: {vendita[1]}, Data: {vendita[2]}\n")

# Funzione per stampare la ricevuta della vendita
def stampa_ricevuta_vendita():
    try:
        articolo_id = int(id_entry.get())
        quantita = int(quantita_entry.get())
        carrello = [{'nome': nome_entry.get(), 'prezzo': float(prezzo_entry.get()), 'quantita': quantita}]
        totale = calcola_totale(carrello)
        stampa_ricevuta(carrello, totale)
        messagebox.showinfo("Ricevuta", "Ricevuta stampata in 'ricevuta.txt'")
    except ValueError:
        messagebox.showerror("Errore", "Controlla i valori di input.")

# Configurazione finestra principale
finestra = tk.Tk()
finestra.title("Programma di Cassa")

# Sezione Aggiungi Articolo
tk.Label(finestra, text="Nome Articolo").pack()
nome_entry = tk.Entry(finestra)
nome_entry.pack()

tk.Label(finestra, text="Prezzo Articolo").pack()
prezzo_entry = tk.Entry(finestra)
prezzo_entry.pack()

tk.Button(finestra, text="Aggiungi Articolo", command=aggiungi).pack()

# Sezione Mostra Articoli
tk.Label(finestra, text="\nElenco Articoli:").pack()
articolo_text = tk.Text(finestra, height=10, width=40)
articolo_text.pack()
tk.Button(finestra, text="Mostra Articoli", command=mostra_tutti_gli_articoli).pack()

# Sezione Vendite
tk.Label(finestra, text="\nID Articolo (per vendita)").pack()
id_entry = tk.Entry(finestra)
id_entry.pack()

tk.Label(finestra, text="Quantità").pack()
quantita_entry = tk.Entry(finestra)
quantita_entry.pack()

tk.Button(finestra, text="Registra Vendita", command=registra).pack()
tk.Button(finestra, text="Calcola Totale", command=calcola_totale_vendita).pack()
tk.Button(finestra, text="Stampa Ricevuta", command=stampa_ricevuta_vendita).pack()

# Sezione Report Vendite
tk.Label(finestra, text="\nReport Vendite:").pack()
report_text = tk.Text(finestra, height=10, width=40)
report_text.pack()
tk.Button(finestra, text="Mostra Report Vendite", command=mostra_report_vendite).pack()

finestra.mainloop()
