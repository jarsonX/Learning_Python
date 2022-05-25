# -*- coding: utf-8 -*-

#import sys
#sys.argv # lista argumetów do programu (można te parametru podawać w cmd)
#         # 20220402_02_pliki.py x=15 y=454
#print(sys.argv)
#
#lista_parametrow = sys.argv[1:]
#slownik = {}
#for parametr in lista_parametrow:
#    l = parametr.split("=")
#    slownik[l[0]]=l[1]
#print(slownik)

import os
#print(os.getcwd()) # Miejsce wywołania skryptu (gdzie znajduje się na dysku)
#print(os.path.sep) # separator w sciezce dostepu
#os.path.join(katalog,plik) => katalog/plik
#print(os.path.join(os.getcwd(),"kot"))
#os.path.exists(xxx)
#os.path.isdir(xxx) czy xxx jest katalogiem
#os.path.isfile(xxx) czy xxx jest plikiem
#print(os.listdir()) # Wszystko, co jest w katalogu

#for nazwa in os.listdir():
#    print(nazwa, os.path.isdir(nazwa), os.path.isfile(nazwa))

"""
open(sciezka_do_pliku,tryb)

Tryby:
    r - do odczytu (plik musi istnieć) -- tryb domyslny
    w - do zapisu (plik jest zawsze tworzony, jeli istnieje, to nadpisuje go pustym)
    a - do dopisywania (jesli plik istnieje, to go otwiera i wskaźki ustawia na końcy, jesli nie istnieje, to tworzy nowy plik)
    
    r+ - odczyt i zapis 
    w+ - zapis i odczyt
    a+ - dopisywanie i odczyt
    
    x - zapis (plik nie może istnieć)
    x+ - zapis i odczyt
"""

####################
#   Odczyt pliku   #
####################

# Funkcja do odczytu całego pliku na raz
def odczyt_1(nazwa_pliku):
    plik = open(nazwa_pliku, 'r')
    
    tekst = plik.read()
    print(tekst)
    plik.close()
    
# to samo, co w odczyt_1, ale prosciej
def odczyt_2(nazwa_pliku):
    tekst = open(nazwa_pliku, 'r').read()
    print(tekst)

# Funkcja do odczytu całego pliku na raz do listy
def odczyt_3(nazwa_pliku):
    lista = open(nazwa_pliku, 'r').readlines()
    print(lista)     
#    for i in range(len(lista)):
#        lista[i] = lista[i].rstrip()
#    lista = list(map(lambda el: el.rstrip(),lista))
#    print(lista)

# Funckja, która odczytuje plik linia po linii (aby oszczędzać pamięć)
def odczyt_po_jedniej_linii(nazwa_pliku):
    plik = open(nazwa_pliku,'r') # zmienna plikowa, aby mieć dowiązanie do pliku
    
    linia = plik.readline() # Odczytanie pierwszej lini
    while linia: # Dopóki są linie, to:
        print(linia) # wywietl
        linia = plik.readline() # wczytaj kolejną

    plik.close()

# Funckja, która odczytuje plik znak po znaku (aby oszczędzać pamięć)
def odczyt_po_jednego_znaku(nazwa_pliku):
    plik = open(nazwa_pliku,'r') # zmienna plikowa, aby mieć dowiązanie do pliku
    
    znak = plik.read(1) # Odczytanie pierwszego znaku
    while znak: # Dopóki są linie, to:
        print(znak, ord(znak)) # wywietl i jego kod ASCII
        znak = plik.read(1) # wczytaj kolejny znak

    plik.close()
    
    
    
#odczyt_1("20220402_01.py")

#odczyt_po_jednego_znaku("plik.txt")

####################
#   Zapis  pliku   #
####################

plik_wy = open("xyz.txt",'w') # Zmienna plikowa, tworzymy nowy plik "xyz.txt"

plik_wy.write("Ala ma kota\n") #\n -- nowa linia
plik_wy.write("kot ma Alę\n")

s = "Ala"
wiek = 43
wzrost = 1.73
#plik_wy.write(str(wiek))

plik_wy.write(f"{s} jest w wieku {wiek} (lat) i ma wstostu: {wzrost} (w metrach).\n")

#lista=["test","test2","test3"]
#plik_wy.writelines(lista) # Zapisuje całą listę łańcuchów znaków do pliku (nie robi nowej lini)
#plik_wy.write("\n".join(lista)) # Analogiczne, własne rozwiązanie, gdzie dodajemy nową linię

plik_wy.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







