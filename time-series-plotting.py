# https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
import pandas as pd
from matplotlib import pyplot as plt
from enum_month import enum_month as em

'''x = [1,2,3]
y = [3,4,1]
z = [10,3,0]
plt.plot(x,y)
plt.plot(x,z)
plt.title("TEST")
plt.xlabel("ICCHESE")
plt.ylabel("UAI e ZETTA")
plt.legend(["QVESTA E' UAI","QVESTA E' ZI"])
plt.show()'''

anno = input("Inserisci il numero di anno: ")
mese_index = input("Inserisci il numero di mese: ")
q = input("Visione per colonne [1] o generica [2] NEW [3]? ")
calc_mese = em(str(mese_index))
mese_numero = calc_mese[0]

if q == "1":
    first_col = pd.read_csv(
        'elaborazioni/' + mese_numero + '_' + str(anno) + '/' + 'first_col_counter_' + mese_numero + '_' + str(
            anno) + '.csv', sep=',')
    second_col = pd.read_csv(
        'elaborazioni/' + mese_numero + '_' + str(anno) + '/' + 'second_col_counter_' + mese_numero + '_' + str(
            anno) + '.csv', sep=',')
    third_col = pd.read_csv(
        'elaborazioni/' + mese_numero + '_' + str(anno) + '/' + 'third_col_counter_' + mese_numero + '_' + str(
            anno) + '.csv', sep=',')
    fourth_col = pd.read_csv(
        'elaborazioni/' + mese_numero + '_' + str(anno) + '/' + 'fourth_col_counter_' + mese_numero + '_' + str(
            anno) + '.csv', sep=',')
    fifth_col = pd.read_csv(
        'elaborazioni/' + mese_numero + '_' + str(anno) + '/' + 'fifth_col_counter_' + mese_numero + '_' + str(
            anno) + '.csv', sep=',')

    plt.plot(fifth_col.iloc[:, 0], fifth_col.iloc[:, 1])
    plt.plot(fourth_col.iloc[:, 0], fourth_col.iloc[:, 1])
    plt.plot(third_col.iloc[:, 0], third_col.iloc[:, 1])
    plt.plot(second_col.iloc[:, 0], second_col.iloc[:, 1])
    plt.plot(first_col.iloc[:, 0], first_col.iloc[:, 1])
    plt.legend(["Fifth Col", "Forth Col", "Third Col", "Second Col", "First Col"])
    plt.show()

elif q == "2":
    general = pd.read_csv(
        'elaborazioni/' + mese_numero + '_' + str(anno) + '/' + 'general_' + mese_numero + '_' + str(anno) + '.csv',
        sep=',')
    dataFrame = general.DataFrame({general.iloc[:, 0], general.iloc[:, 1]})
    ax = dataFrame.plot.bar()
    #plt.plot(general.iloc[:, 0], general.iloc[:, 1])
    plt.show()

elif q == "3":
    first_col = pd.read_csv(
        'elaborazioni/' + mese_numero + '_' + str(anno) + '/' + 'first_col_counter_' + mese_numero + '_' + str(
            anno) + '.csv', sep=',')
    plt.plot(first_col.iloc[:, 0], first_col.iloc[:, 1])
    plt.show()


#a = general.groupby(['Ricorrenze']).mean().sort_values('Ricorrenze', ascending=True)
#print(a)
