from enum_month import enum_month as em

import json
import csv
import os
import wget

index = 1

with open("mega_inzuppone_1_col.csv", mode="w") as ext_file:
    ext_file_writer = csv.writer(ext_file)
    ext_file_writer.writerow(["ID", "Numero"])
    for anni_range in range(2015, 2020):
        for mese_range in range(1, 13):
            calc_mese = em(str(mese_range))
            mese_numero = calc_mese[0]
            with open("estrazioni/" + str(anni_range) + "/" + str(mese_numero) + ".csv") as f:
                extracted = csv.reader(f)
                next(extracted, None)
                for rows in extracted:
                    ext_file_writer.writerow([str(index), rows[0]])
                    index += 1