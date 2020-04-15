from general_cvs_data_creator import general_csv_data_generator as gc
from column_cvs_data_creator import col_csv_data_extractor as cc
from enum_month import enum_month as em

print("\nBenvenuto nell'estrattore dati!\n")

extr_a = False
extr_b = False
extr_c = False

a = input("\nEngine A [1], B [2] o C [3]? ")

if a == "1":
    extr_a = True
elif a == "2":
    extr_b = True
elif a == "3":
    extr_c = True
else:
    print("[!] Arg not valid")

### Estrazione automatica dei dati, dati i registri esistenti in archivio. Presenti 3 wave:
### 1) Estrazione dei valori dal primo registrato (07/2014) all'ultimo del 2014;
### 2) Dal 01/2015 al 12/2019
### 3) Dal 01/2020 ad oggi

# 1)
if extr_a:
    for mese_index in range(7, 13):
        calc_mese = em(str(mese_index))
        mese = calc_mese[1]
        mese_numero = calc_mese[0]
        print("\nEseguo il mese: " + mese_numero + "/" + str(2014))
        gc(mese, mese_numero, str(2014))
        cc(mese, mese_numero, str(2014))

# 2)
if extr_b:
    for anno in range(2015, 2020):
        for mese_index in range(1, 13):
            calc_mese = em(str(mese_index))
            mese = calc_mese[1]
            mese_numero = calc_mese[0]
            print("\nEseguo il mese: " + mese_numero + "/" + str(anno))
            gc(mese, mese_numero, str(anno))
            cc(mese, mese_numero, str(anno))

# 3)
if extr_c:
    print("\nEseguo il mese: 01" + "/" + str(2020))
    gc("gennaio", "01", str(2020))
    cc("gennaio", "01", str(2020))


### A seguire estrazione manuale. Pronto da lanciare, chiede gli argomenti da riga di comando
'''
anno = input("Inserisci l'anno: ")
mese_numero = input("Inserisci il mese: ")

calc_mese = em(mese_numero)
mese = calc_mese[1]
mese_numero = calc_mese[0]

extraction_kind = input("Estrazione globale [1], colonnare [2] o mista [3]? ")

if extraction_kind == "1":
    gc(mese, mese_numero, anno)

elif extraction_kind == "2":
    cc(mese, mese_numero, anno)

elif extraction_kind == "3":
    gc(mese, mese_numero, anno)
    cc(mese, mese_numero, anno)
else:
    print("Fine senza alcuna operazione!")
    
'''
