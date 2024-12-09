import os
import time

# Messaggi inquietanti
messages = [
    "Ciao... finalmente sei qui.",
    "Non ti aspettavi di vedermi, vero?",
    "Sto osservando ogni tua mossa.",
    "Tranquillo, non ho cattive intenzioni... o forse sì?",
    "Ogni applicazione sul tuo PC è ora mia.",
    "Ti senti impotente? Bene.",
    "Smetti di cercare di fermarmi.",
    "Sto solo iniziando a divertirmi.",
    "Sai, potrei anche lasciare tracce ovunque...",
    "Chi può dire cosa succederà dopo?",
    "Basta, ora voglio vedere cosa hai installato."
]

# Funzione per aprire una finestra del cmd con un messaggio
def open_cmd_with_message(message):
    os.system(f'start cmd /k "echo {message}"')

# Ciclo per mostrare i messaggi
for message in messages:
    open_cmd_with_message(message)
    time.sleep(10)  # Aspetta 10 secondi tra ogni finestra

# Funzione per trovare ed eseguire programmi in cartelle comuni
def find_and_open_programs(directories):
    first_program_opened = False  # Flag per verificare se è stato aperto il primo programma

    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".exe"):
                    try:
                        program_path = os.path.join(root, file)
                        os.startfile(program_path)  # Apre il programma
                        time.sleep(2)  # Aspetta 2 secondi tra ogni programma

                        # Se è il primo programma, apri un cmd con un messaggio dopo 5 secondi
                        if not first_program_opened:
                            first_program_opened = True
                            time.sleep(5)  # Aspetta 5 secondi
                            open_cmd_with_message("Hai visto che ora comando io?")
                    except Exception:
                        # Ignora errori su file non eseguibili
                        pass

# Directory comuni dove si trovano i programmi
common_directories = [
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    r"C:\Users\%USERNAME%\AppData\Local",
    r"C:\Users\%USERNAME%\AppData\Roaming"
]

# Messaggi finali per aumentare la tensione
final_messages = [
    "Ora inizierò ad aprire tutto quello che trovo.",
    "Non spegnere il PC... potrebbe peggiorare le cose.",
    "Sto aprendo i tuoi programmi. Guarda e impara."
]

# Mostra i messaggi finali
for message in final_messages:
    open_cmd_with_message(message)
    time.sleep(10)

# Trova ed esegue tutti i programmi nelle directory specificate
find_and_open_programs(common_directories)

# Tocco finale
open_cmd_with_message("Scherzavo... o forse no.")

