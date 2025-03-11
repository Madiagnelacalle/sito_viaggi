from os import system
volo_1 = {
    "ID": 300,
    "nome": "primo",
    "destinazione": "Roma",
    "data": "2025-09-30",
}
volo_2 = {
    "ID": 120,
    "nome": "secondo",
    "destinazione": "Roma",
    "data": "2025-09-30",
}
destinazioni = [    
    "Roma", 
    "Parigi", 
    "Berlino", 
    "Madrid", 
    "Londra", 
    "Amsterdam", 
    "Vienna", 
    "Praga", 
    "Budapest", 
    "Atene"
]
date = [
    "2025-03-11",
    "2025-07-22",
    "2025-05-15",
    "2025-09-30",
    "2025-12-05",
    "2025-01-18",
    "2025-04-27",
    "2025-08-14",
    "2025-06-09",
    "2025-11-03"
]
viaggi= [volo_1, volo_2]
def destinazione_visualizza(lista):
    print("Ecco le destinazioni europee disponibili:")
    for i in range(len(lista)):
        print(f"||{lista[i]}|| ")
def date_visualizza(lista):
    print("Ecco le date disponibili:")
    for i in range(len(lista)):
        print(f"||{lista[i]}||")
def aggiungi_viaggio(lista,destinazioni,date):
 
    errore_id = True
    while errore_id == True:
        id_viaggi = int(input("inserisci l'id del viaggio: "))
        for i in range(len(lista)):
            if lista[i]["ID"] == id_viaggi:
                print("non puoi inserire due viaggi con lo stesso id")
                errore_id = True
                break
            else:
                errore_id = False
    nome = input("inserisci il nome: ")
    errore_destinazione = True
    destinazione_visualizza(destinazioni)
    while errore_destinazione == True:
        destinazione = input("inserisci la destinazione: ")
        if destinazione not in destinazioni:
            print()
            print("La destinazione deve essere presente all'interno delle destinazioni ")
            errore_destinazione = True
            continue
            print()
        else:
            errore_destinazione = False
    errore_data = True
    date_visualizza(date)
    while errore_data == True:
        data = input("inserisci la data: ")
        if data not in date:
            errore_data = True
            print()
            print("La data deve essere presente all'interno delle date presenti")
            errore_data = True
            print()
            continue
        else:
            errore_data = False

 
    volo = {
        "ID" : id_viaggi,
        "nome" : nome,
        "destinazione" : destinazione,
        "data" : data
        }
    lista.append(volo)
def scheda_viaggi(lista):
    for s in range(len(lista)):
        for i in lista[s].keys():
            print(f" {i} - {lista[s][i]} ")
        print()    
def rimuovi_viaggio(lista):
    errore = True
    scheda_viaggi(lista)
    while errore == True:
        indice = int(input("inserisci l'ID del viaggio da rimuovere:  "))
        c = 0
        s = 0
        while c < len(lista):
            id = lista[c]["ID"]
            if indice == id:     
                lista.remove(lista[c])
                s += 1
                errore = False
            c += 1
        if s == 0:
            print("l'ID inserito non è presente all'interno della lista di viaggi")
            print()
            print()
            errore = True
    print("Ecco la lista di viaggi aggiornata")
    print()
    scheda_viaggi(lista)

 
def modifica(lista,destinazioni,date):
    scheda_viaggi(lista)
    print()
    id_viaggio = int(input("Digitare il ID del viaggio da modificare: "))
    count = 0
    print()
    while count < len(lista):
        if id_viaggio == lista[count]["ID"]:
            print("Cosa si vuole modificare?")
            print("\t1. ID\n\t2. Nome\n\t3. Destinazione\n\t4. Data")
            scelta = int(input("--> "))
            if scelta == 1:
                nuovo_id = int(input("Digitare il nuovo ID: "))
                lista[count]["ID"] = nuovo_id 
            elif scelta == 2:
                nuovo_nome = input("Digitare il nuovo nome: ")
                lista[count]["nome"] = nuovo_nome
            elif scelta == 3:
                destinazione_visualizza(destinazioni)
                nuova_destinazione = input("Digitare la nuova destinazione: ")
                lista[count]["destinazione"] = nuova_destinazione 
            elif scelta == 4:
                date_visualizza(date)
                nuova_data = input("Digitare la nuova data: ")
                lista[count]["data"] = nuova_data
            else:
                print("Scelta non valida")
                break
        count +=1
 
def visualizza_viaggio(lista):
    scheda_viaggi(lista)
    id_viaggio = int(input("Inserire ID del viaggio da visualizzare: "))
    count = 0
    while count < len(lista):
        if id_viaggio == lista[count]["ID"]:
            print(f"ID: {lista[count]['ID']}\nNome: {lista[count]['nome']}\nDestinazione: {lista[count]['destinazione']}\nData: {lista[count]['data']}")
            return
        count +=1
    print("ID del viaggio non trovato")
    return -1

 
def visualizza_destinazione(lista,destinazioni):
    destinazione_visualizza(destinazioni)
    destinazione = input("Inserisci la destinazione comune da visualizzare: ")
    for i in range(len(lista)):
        if lista[i]["destinazione"] == destinazione:
            for s in lista[i].keys():
                print(f"{s} - {lista[i][s]}")
            print()

 
def visualizza_data(lista, data):
    date_visualizza(date)
    data = input("Inserisci la data comune da visualizzare: ")
    for i in range(len(lista)):
        if lista[i]["data"] == data:
            for s in lista[i].keys():
                print(f"{s} - {lista[i][s]}")
            print()

def menu():
    system("cls")
    print("╔════════════════════════════════════════╗")
    print("║               MENU VIAGGI              ║")
    print("╠════════════════════════════════════════╣")
    print("║ 1. Aggiungere un viaggio               ║")
    print("║ 2. Rimuovere un viaggio                ║")
    print("║ 3. Modificare un viaggio               ║")
    print("║ 4. Visualizzare tutti i viaggi         ║")
    print("║ 5. Visualizzare un viaggio tramite ID  ║")
    print("║ 6. Visualizzare viaggi per destinazione║")
    print("║ 7. Visualizzare viaggi per data        ║")
    print("║ 8. Chiusura del programma              ║")
    print("╚════════════════════════════════════════╝")
    print()
    scelta = 0
    while scelta >= 0 and scelta <= 8:
        scelta = int(input("Fai la tua scelta: "))
        try:
            if scelta == 1:
                aggiungi_viaggio(viaggi,destinazioni,date)
                print(viaggi)
            if scelta == 2:
                rimuovi_viaggio(viaggi)
            if scelta == 3:
                modifica(viaggi,destinazioni,date)
            if scelta == 4:
                scheda_viaggi(viaggi)
            if scelta == 5:
                visualizza_viaggio(viaggi)
            if scelta == 6:
                visualizza_destinazione(viaggi,destinazioni)
        except ValueError:
            print("ValueError: input non valido")
        except:
            print("Qualcosa è andato storto")
        finally:
            input("premere un tasto per continuare....")
menu()
