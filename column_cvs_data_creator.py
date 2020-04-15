import json
import csv
import os
import wget

'''### EDIT HERE! ###
mese = "dicembre"
mese_numero = "12"
anno = "2019"
##################'''


def col_csv_data_extractor(mese, mese_numero, anno):
    estrazioni = []
    counter_partial = []

    print("\nBenvenuto nel Column CSV Data Extractor!")
    # Definisco un array dove andrò a caricare i pesi delle varie ricorrenze
    for i in range(1, 41):
        counter_partial.append([i, 0])

    # Creo la cartella riferita a quell'anno/mese se non presente
    path_result = "elaborazioni/" + mese_numero + "_" + anno
    if not os.path.isdir(path_result):
        os.mkdir("elaborazioni/" + mese_numero + "_" + anno)
        print("[+] Creata la cartella: /elaborazioni/" + mese_numero + "_" + anno)

    path_extraction = "estrazioni/" + anno
    if not os.path.isdir(path_extraction):
        os.mkdir("estrazioni/" + anno)
        print("[+] Creata la cartella: /estrazioni/" + anno)

    print("[+] Tutte cartelle necessarie presenti!")

    # Estraggo il JSON dal sito SE non presente
    sisal_file = "raw_data/" + mese_numero + "_" + anno + ".json"
    if not os.path.isfile(sisal_file):
        url = "http://www.vincicasa.it/sisal-gn-proxy-servlet-web/proxy/gntn-info-web/rest/gioco/vincicasa/estrazioni" \
              "/archivioconcorso/" + anno + "/" + mese_numero
        file = wget.download(url, "raw_data/" + mese_numero + "_" + anno + ".json")
        print("[!] Download effettuato del file: " + mese_numero + "_" + anno + ".json")
    else:
        print("[!] Dati già presenti")

# Estraggo i numeri sorteggiati dal JSON di SISAL SE non presenti
    with open("estrazioni/" + anno + "/" + mese_numero + ".csv", mode="w") as ext_file:
        ext_file_writer = csv.writer(ext_file)
        ext_file_writer.writerow(["Extr1", "Extr2", "Extr3", "Extr4", "Extr5"])
        with open("raw_data/" + mese_numero + "_" + anno + ".json") as f:
            data = json.loads(f.read())
            for items in data["concorsi"]:
                estrazioni.append(items['combinazioneVincente']["estratti"])
                ext_file_writer.writerow(items['combinazioneVincente']["estratti"])
        print("[++] Parsing del JSON effettuato con Successo!")

    # Scrivo su file ricorrenze dei numeri visti per colonne
    for indicino in range(0, 5):

        if indicino == 0:
            extracted_file = "elaborazioni/" + mese_numero + "_" + anno + "/" + "first_col_counter_" + mese_numero + "_" + anno + ".csv"
            if not os.path.isfile(extracted_file):
                with open(
                        "elaborazioni/" + mese_numero + "_" + anno + "/" + "first_col_counter_" + mese_numero + "_" + anno + ".csv",
                        mode="w") as ext_file:
                    ext_file_writer = csv.writer(ext_file)
                    ext_file_writer.writerow(["Numero", "Ricorrenze"])

                    # Azzero l'array
                    counter_partial = []
                    for i in range(1, 41):
                        counter_partial.append([i, 0])

                    for value in range(len(estrazioni)):
                        counter_partial[int(estrazioni[value][indicino]) - 1][1] += 1
                    for indice in range(40):
                        ext_file_writer.writerow(counter_partial[indice])
                print("[+++] Prima colonna estratta con successo!")
            else:
                print("[!] CSV già presente!")

        elif indicino == 1:
            extracted_file = "elaborazioni/" + mese_numero + "_" + anno + "/" + "second_col_counter_" + mese_numero + "_" + anno + ".csv"
            if not os.path.isfile(extracted_file):
                with open(
                        "elaborazioni/" + mese_numero + "_" + anno + "/" + "second_col_counter_" + mese_numero + "_" + anno + ".csv",
                        mode="w") as ext_file:
                    ext_file_writer = csv.writer(ext_file)
                    ext_file_writer.writerow(["Numero", "Ricorrenze"])

                    counter_partial = []
                    for i in range(1, 41):
                        counter_partial.append([i, 0])

                    for value in range(len(estrazioni)):
                        counter_partial[int(estrazioni[value][indicino]) - 1][1] += 1
                    for indice in range(40):
                        ext_file_writer.writerow(counter_partial[indice])
                print("[+++] Seconda colonna estratta con successo!")
            else:
                print("[!] CSV già presente!")

        elif indicino == 2:
            extracted_file = "elaborazioni/" + mese_numero + "_" + anno + "/" + "third_col_counter_" + mese_numero + "_" + anno + ".csv"
            if not os.path.isfile(extracted_file):
                with open(
                        "elaborazioni/" + mese_numero + "_" + anno + "/" + "third_col_counter_" + mese_numero + "_" + anno + ".csv",
                        mode="w") as ext_file:
                    ext_file_writer = csv.writer(ext_file)
                    ext_file_writer.writerow(["Numero", "Ricorrenze"])

                    counter_partial = []
                    for i in range(1, 41):
                        counter_partial.append([i, 0])

                    for value in range(len(estrazioni)):
                        counter_partial[int(estrazioni[value][indicino]) - 1][1] += 1
                    for indice in range(40):
                        ext_file_writer.writerow(counter_partial[indice])
                print("[+++] Terza colonna estratta con successo!")
            else:
                print("[!] CSV già presente!")

        elif indicino == 3:
            extracted_file = "elaborazioni/" + mese_numero + "_" + anno + "/" + "fourth_col_counter_" + mese_numero + "_" + anno + ".csv"
            if not os.path.isfile(extracted_file):
                with open(
                        "elaborazioni/" + mese_numero + "_" + anno + "/" + "fourth_col_counter_" + mese_numero + "_" + anno + ".csv",
                        mode="w") as ext_file:
                    ext_file_writer = csv.writer(ext_file)
                    ext_file_writer.writerow(["Numero", "Ricorrenze"])

                    counter_partial = []
                    for i in range(1, 41):
                        counter_partial.append([i, 0])

                    for value in range(len(estrazioni)):
                        counter_partial[int(estrazioni[value][indicino]) - 1][1] += 1
                    for indice in range(40):
                        ext_file_writer.writerow(counter_partial[indice])
                print("[+++] Quarta colonna estratta con successo!")
            else:
                print("[!] CSV già presente!")

        else:
            extracted_file = "elaborazioni/" + mese_numero + "_" + anno + "/" + "fifth_col_counter_" + mese_numero + "_" + anno + ".csv"
            if not os.path.isfile(extracted_file):
                with open(
                        "elaborazioni/" + mese_numero + "_" + anno + "/" + "fifth_col_counter_" + mese_numero + "_" + anno + ".csv",
                        mode="w") as ext_file:
                    ext_file_writer = csv.writer(ext_file)
                    ext_file_writer.writerow(["Numero", "Ricorrenze"])

                    counter_partial = []
                    for i in range(1, 41):
                        counter_partial.append([i, 0])

                    for value in range(len(estrazioni)):
                        counter_partial[int(estrazioni[value][indicino]) - 1][1] += 1
                    for indice in range(40):
                        ext_file_writer.writerow(counter_partial[indice])
                print("[+++] Quinta colonna estratta con successo!")
            else:
                print("[!] CSV già presente!")
    print("[++++] Script eseguito con successo! File generato dentro: /elaborazioni/" + mese_numero + "_" + anno + "/")
