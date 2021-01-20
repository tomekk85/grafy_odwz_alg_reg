import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from my3d import *
from my2d import *


wyb_wym_lista = vert5x5
wyb_graf = "5x5"
wyb_par = 2 #0-7



D = np.array([[1, 0],
              [0, 1]])
print("macierz D")
print(D)
print(50 * '-')

list_ = []

for i in range(-1, 2):
    for j in range(-1, 2):
        if not (i == 0 and j == 0):
            list_.append(np.array([i, j]))
print("Potencjalne możliwości")

# funkcja pomocnicza do wydruków list(usuwa napis "array" i nawiasy okrągłe)
def replArrStr(string):
    return string.replace("array", "").replace("(", "").replace(")", "")

print(replArrStr(str(list_)))
print(50 * '-')

#dla każego d Fs * d == -1 lub Fs == 0 lub Fs == 1
print("Warunek lokalności:")
print("dla każego d Fs * d == -1 lub Fs * d == 0 lub Fs * d == 1")
list_of_FSs = []
for i in range(0, len(list_)):
    D_x_Fs = np.dot(D, list_[i])
    print(str(i) + ". D*list_=" + str(D_x_Fs) + " FsPot = " + str(list_[i]))

    if (D_x_Fs[0] == -1 or D_x_Fs[0] == 0 or D_x_Fs[0] == 1) \
            and (D_x_Fs[1] == -1 or D_x_Fs[1] == 0 or D_x_Fs[1] == 1):
        # if (D_x_Fs[0] == -1 and D_x_Fs[1] == -1) or (D_x_Fs[0] == 0 and D_x_Fs[1] == 0) \
        #        or (D_x_Fs[0] == 1 and D_x_Fs[1] == 1):
        list_of_FSs.append(list_[i])

print("Lista Fs, które spełniają warunek lokalności")
print(replArrStr(str(list_of_FSs)))
print(50 * '-')


print("Warunek przyczynowości:")
print("dla każego d Ft * d >= 1")

list_of_FTs = []
for i in range(0, len(list_)):
    D_x_Ft = np.dot(D, list_[i])
    print(str(i) + ". D*list_=" + str(D_x_Ft) + " FtPot = " + str(list_[i]))

    if D_x_Ft[0] >= 1 and D_x_Ft[1] >= 1:
        list_of_FTs.append(list_[i])

print("Lista Ft, które spełniają warunek przyczynowości")
print(replArrStr(str(list_of_FTs)))
print(50 * '-')

list_merged = []
print("Lista par [Fs], [Ft] możliwych do wykorzystania:")

for D_x_Fs in list_of_FSs:
    for ft in list_of_FTs:
        list_merged.append(np.array([D_x_Fs, ft]))

# array[Fs, Ft]
lmcounter = 0

for item in list_merged:
    print("para " + str(lmcounter) + " Fs=" + str(item[0]) + ", Ft=" + str(item[1]))
    #print(str(item).replace("array", ""))
    lmcounter += 1
print(50 * '-')
wyb_par = int(input('Wybierz parę[0-7]:'))

print("\nWybrany przypadek - para: " + str(wyb_par))
print('Fs=' + str(list_merged[wyb_par][0]) + ', Ft=' + str(list_merged[wyb_par][1]))

# wierzchołki (dla macierzy 5x5)
list_i = [1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5], [1, 1], [2, 2], [3, 3], \
         [4, 4], [5, 5]


list_aurelia = [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]


list_i = wyb_wym_lista



#list_i = list_aurelia
# list wierzchołków
list_v = []
for item in list_i:
    list_v.append(np.array(item))
# sortowanie
list_v.sort(key=lambda x: x[1])
list_v.sort(key=lambda x: x[0])
print("Lista wierzchołków:")
print(replArrStr(str(list_v)))
input("Wciśnij Enter by kontynuować...")

inp_ = list_merged[wyb_par]



counter = 1

# elementy przetwarzające zbieramy do słownika

dict_p = {} # słownik elemntów przetwarzających

print("\nElementy przetwarzające.")
for wierzch in list_v:
    el_p = np.dot(wierzch, inp_[0])
    takt = np.dot(wierzch, inp_[1])
    print(
        str(counter) + ". K=" + str(wierzch) + " ||| Fs * K (el. przetw)= " + str(el_p)
        + " ||| Ft * K (takt) = " + str(takt)
    )

    upd = []
    if dict_p.get(el_p) is None:
        upd = [[counter, takt, wierzch]]
    else:
        upd = dict_p.get(el_p)
        upd.append([counter, takt, wierzch])
    dict_p.update({el_p: upd})

    counter += 1
input("Wciśnij Enter by kontynuować...")

# sortujemy słownik rosnąco wg klucza (el przetwarzający)
import collections

dict_p_ord = collections.OrderedDict(sorted(dict_p.items()))

print("\nGrupujemy wierzchołki w poszczególnych elementach przetwarzających.")
for key in dict_p_ord:
    print("Ep[" + str(key) + "]")
    for row in dict_p_ord.get(key):
        print(str(row[0]) + '. wierzch.=' + str(row[2]) + ' takt=' + str(row[1]))

input("Wciśnij Enter by kontynuować...")

napis_FsFt = ' dla Fs=' + str(list_merged[wyb_par][0]) + ', Ft=' + str(list_merged[wyb_par][1])

Subplot().draw(wyb_graf, dict_p_ord, napis_FsFt)

