import os

volo_1 = {
    "ID": 300,
    "nome": "primo",
    "destinazione": "roma",
    "data": 250720,
}
volo_2 = {
    "ID": 120,
    "nome": "secondo",
    "destinazione": "napoli",
    "data": 251201,
}

viaggi= [volo_1, volo_2]

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

def visualizza_viaggio(lista):
    id_viaggio = int(input("Inserire ID del viaggio da visualizzare: "))
    count = 0
    while count < len(lista):
        if id_viaggio == lista[count]["ID"]:
            print(f"ID: {lista[count]['ID']}\nNome: {lista[count]['nome']}\nDestinazione: {lista[count]['destinazione']}\nData: {lista[count]['data']}")
            return
        count +=1
    print("ID del viaggio non trovato")
    return -1
    
def scheda_viaggi(lista):
    count = 0
    while count < len(lista):
        print(f"{lista[count]}")
        count +=1
    return
