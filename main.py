import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from my3d import *
from my2d import *

#luk = LUplot()
#luk.draw('luk')
#4,5,6,8,10
dict_n = {4: [vert4x4, "4x4"], 5: [vert5x5, "5x5"], 6: [vert6x6, "6x6"], 8: [vert8x8, "8x8"],   10: [vert10x10, "10x10"]}

n = dict_n.get(int(
    input("Wybierz wymiar(n) macierzy[4, 5, 6, 8, 10]:")
))
wyb_wym_lista = n[0]
wyb_graf = n[1]
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
takty = [] # tablica taktów
dict_2ep ={} # słownik wykorzystany do obliczenia złożoności sprzętowej macierzy procesorowej

print("\nElementy przetwarzające.")
for wierzch in list_v:
    el_p = np.dot(wierzch, inp_[0])
    takt = np.dot(wierzch, inp_[1])
    takty.append(takt)
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
print(50 * '-')
input("Wciśnij Enter by kontynuować...")

# sortujemy słownik rosnąco wg klucza (el przetwarzający)
import collections

dict_p_ord = collections.OrderedDict(sorted(dict_p.items()))

print("\nGrupujemy wierzchołki w poszczególnych elementach przetwarzających.")
for key in dict_p_ord:
    print("Ep[" + str(key) + "]")
    klucz = key# złożoność
    for row in dict_p_ord.get(key):
        oper = '"* +" '
        if row[2][0] == row[2][1]:
            oper = '"/"'
            dict_2ep.update({klucz: str(dict_2ep.get(klucz)) + " " + oper}) # złożoność
        else:
            dict_2ep.update({klucz: str(dict_2ep.get(klucz)) + " " + oper})  # złożoność

        print(str(row[0]) + '. wierzch.=' + str(row[2]) + ' takt=' + str(row[1]) + " operacja " + oper)
print(50 * '-')
input("Wciśnij Enter by kontynuować...")

napis_FsFt = ' dla Fs=' + str(list_merged[wyb_par][0]) + ', Ft=' + str(list_merged[wyb_par][1])


Fmax = 354
EPLatency = 24
max_ = max(takty)
min_ = min(takty)
liczba_el_p = len(dict_p_ord)

print("Przyjmujemy, że")
print("Fmax=354MHz, EPlatency=24")
print("Korzystając z poniższego wzoru obliczamy Ts:")
print("Ts = (Liczba_Ep * Ep_latency + (Ep_max - Ep_min) + 1) / Fmax")
Ts = (liczba_el_p * EPLatency + (max_ - min_) + 1) / Fmax
print("Ts = " + str(round(Ts, 5)) + " us")
print(50 * '-')

#mult, lut mem
dziel = np.array([7, 1175, 3])
dod_mnoz = np.array([2, 1311, 0])
razem = dziel + dod_mnoz


for key in dict_2ep:
    if dict_2ep.get(key).find('"* +"') != -1 and dict_2ep.get(key).find('"/"') != -1:
        dict_2ep.update({key: razem})
    elif dict_2ep.get(key).find('"* +"') != -1:
        dict_2ep.update({key: dod_mnoz})
    elif dict_2ep.get(key).find('"/"') != -1:
        dict_2ep.update({key: dziel})


result = np.array([0, 0, 0])
for key in dict_2ep:
    result += dict_2ep.get(key)

print("Złożoność sprzętowa macierzy procesorowej dla n=" + wyb_graf[0]  + ":")
Fs = str(list_merged[wyb_par][0])
Ft = str(list_merged[wyb_par][1])
print("Fs=" + Fs + ", Ft=" + Ft)
print("mult=" + str(result[0]) + ", lut=" + str(result[1]) + " ,mem=" + str(result[2]))

Subplot().draw(wyb_graf, dict_p_ord, napis_FsFt)

