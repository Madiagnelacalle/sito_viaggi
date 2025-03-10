import os

viaggi = {}

def aggiungi_viaggio():
    id_viaggio = input("Inserisci ID viaggio: ")
    while id_viaggio in viaggi:
        print("ID già esistente. Riprova.")
        id_viaggio = input("Inserisci ID viaggio: ")
    
    nome = input("Inserisci nome: ")
    destinazione = input("Inserisci destinazione: ")
    data = input("Inserisci data: ")
    viaggi[id_viaggio] = {"nome": nome, "destinazione": destinazione, "data": data}
    return f"Viaggio aggiunto: {viaggi[id_viaggio]}"

def rimuovi_viaggio():
    id_viaggio = input("Inserisci ID viaggio da rimuovere: ")
    while id_viaggio not in viaggi:
        id_viaggio = input("Viaggio non trovato. Riprova: ")
    viaggi.pop(id_viaggio)
    return f"Viaggio {id_viaggio} rimosso con successo."

def modifica_viaggio():
    id_viaggio = input("Inserisci ID viaggio da modificare: ")
    while id_viaggio not in viaggi:
        id_viaggio = input("Viaggio non trovato. Riprova: ")
    
    nome = input("Nuovo nome (lascia vuoto per non cambiare): ")
    destinazione = input("Nuova destinazione (lascia vuoto per non cambiare): ")
    while destinazione and len(destinazione) < 3:
        destinazione = input("La destinazione deve avere almeno 3 caratteri. Riprova: ")
    
    data = input("Nuova data (lascia vuoto per non cambiare): ")
    if nome:
        viaggi[id_viaggio]["nome"] = nome
    if destinazione:
        viaggi[id_viaggio]["destinazione"] = destinazione
    if data:
        viaggi[id_viaggio]["data"] = data
    
    return f"Viaggio modificato: {viaggi[id_viaggio]}"
