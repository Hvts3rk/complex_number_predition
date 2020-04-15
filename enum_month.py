def enum_month(mese_numero):

    if mese_numero == "1":
        return ["01","gennaio"]
    elif mese_numero == "2":
        return ["02","febbraio"]
    elif mese_numero == "3":
        return ["03","marzo"]
    elif mese_numero == "4":
        return ["04","aprile"]
    elif mese_numero == "5":
        return ["05","maggio"]
    elif mese_numero == "6":
        return ["06","giugno"]
    elif mese_numero == "7":
        return ["07", "luglio"]
    elif mese_numero == "8":
        return ["08","agosto"]
    elif mese_numero == "9":
        return ["09","settembre"]
    elif mese_numero == "10":
        return ["10","ottobre"]
    elif mese_numero == "11":
        return ["11", "novembre"]
    elif mese_numero == "12":
        return ["12","dicembre"]
    else:
        print("[-] Errore! Codice mese non corretto!")
        exit(0)