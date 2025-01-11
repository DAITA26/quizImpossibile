import random

domande = ("A quale colore sto pensando?",
           "A quale città sto pensando?",
           "A quale frutto sto pensando?" ,
           "A quale animale sto pensando?" ,
           "A quale professione sto pensando?")

#colori = {"A" : "Magenta", "B" : "Vinaccia", "C" : "Bordeaux", "D" : "Cremisi"}
#città = {"A" : "Milano", "B" : "Roma", "C" : "Bari", "D" : "Catania"}
#frutti = {"A" : "Mango", "B" : "Cocco", "C" : "Mela", "D" : "Pera"}
#animali = {"A" : "Elefante", "B" : "Volpe", "C" : "Leone", "D" : "Tigre"}
#professioni = {"A" : "Idraulico", "B" : "Cameriere", "C" : "Manager", "D" : "Avvocato"}

opzioni = {
    0: ["Magenta", "Vinaccia", "Bordeaux", "Cremisi"],
    1: ["Milano", "Roma", "Bari", "Catania"],
    2: ["Mango", "Cocco", "Mela", "Pera"],
    3: ["Elefante", "Volpe", "Leone", "Tigre"],
    4: ["Idraulico", "Cameriere", "Manager", "Avvocato"]
    }


risposte_corrette = []

risposte_utente = []

# Punteggio iniziale
punteggio = 0
    #ripetere domande
for i, domanda in enumerate(domande):
    print(f"Domanda {i + 1}: {domanda}")
    # opzioni di risposta
    for j, opzione in enumerate(opzioni[i]):
        print(f"{j + 1}. {opzione}")

    # La macchina sceglie una risposta giusta a caso
    risposta_corretta = random.randint(0, 3)
    risposte_corrette.append(risposta_corretta)

    risposta_utente = -1
    while risposta_utente not in range(4):
        risposta_utente = int(input("Inserisci il numero della tua risposta: ")) - 1

    risposte_utente.append(risposta_utente)


    if risposta_utente == risposta_corretta:
        print("Risposta corretta!\n")
        punteggio += 1
    else:
        print(f"Sbagliato! La risposta corretta era: {opzioni[i][risposta_corretta]}\n")


print(f"Il tuo punteggio finale è: {punteggio}/{len(domande)}")

#Calcola e stampa il rateo di vittoria
vittorie = sum(1 for c, u in zip(risposte_corrette, risposte_utente) if c == u)
rateo_vittoria = (vittorie / len(domande)) * 100
print(f"\nRateo di vittoria: {rateo_vittoria:.2f}%")