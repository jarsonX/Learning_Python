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
    

#_________________________________________________________________

import os

my_dir: str = r"C:\Users\krzys\Desktop"


'''PATHS, FILES & DIRECTORIES

os.getcwd()     # Miejsce wywołania skryptu.
os.path.sep     # Separator odpowiedni dla danego OS.
                # Przydatne przy łączeniu dir i file nam w path.

os.path.join(dir_path, file) # Łączy directory i file name w path.
    
os.path.exists(path)    # Sprawdza czy path istnieje.
os.path.isdir(path)     # Sprawdza czy pod path jest katalog.
os.path.isfile(path)    # Sprawdza czy pod path jest plik.

os.listdir()    # Zwraca zawartosć katalogu w formie listy.'''

# print("The directory contains:")
# for a_file in os.listdir(my_dir):
#     print(a_file)
    
# print("\nThe file paths are:")
# for a_file in os.listdir(my_dir):
#     print(os.path.join(my_dir, a_file))


'''HANDLING FILES'''

# Odczyt calego pliku
def read_a_file(file_path):
    text = open(file_path).read()
    print(text)
    text.close()

# Odczyt pliku do listy
def read_to_list(file_path):
    a_list = open(file_path).readlines()
    print(a_list)
    a_list.close()
    
# Odczyt pliku do listy (usuwa whitespaces)
def read_to_list_2(file_path):
    a_list = open(file_path).readlines()
    for i in range(len(a_list)):
        a_list[i] = a_list[i].rstrip()
    # a_list = list(map(lambda el: el.strip(), a_list))  # Alternatywa dla for
    print(a_list)
    a_list.close()
    
# Odczyt pliku linia po linii (oszczędza pamięć)
def read_by_line(file_path):
    a_file = open(file_path)
    a_line = a_file.readline()
    while a_line:
        print(a_line)
        a_line = a_file.readline()
    a_file.close()

# Odczyt znak po znaku
def read_by_char1(file_path):
    a_file = open(file_path)
    char = a_file.read(1)
    while char:
        print(char, ord(char))
        char = a_file.read(1)
    a_file.close()

# Odczyt znak po znaku z pominięciem kodu ASCII spacji.
def read_by_char2(file_path):
    a_file = open(file_path)
    char = a_file.read(1)
    while char:
        if ord(char) != 10:
            print(char, ord(char))
        else:
            print()
        char = a_file.read(1)
    a_file.close()

   
#read_by_char2(r"C:\Users\krzys\Desktop\UE\Python\Kody z zajęć\test\xyz.txt")

'''COUNTING NUMBERS'''

# Sumowanie wszystkich liczb (a nie cyfr)
def sum_numbers(file_path):
    a_file = open(file_path).read()
    a_file = a_file.split()  # Dzieli po spacjach.
    my_sum = 0
    for a_number in a_file:
        try:
            my_sum += float(a_number)
        except:
            pass
    return my_sum

print(sum_numbers(r"C:\Users\krzys\Desktop\UE\Python\Kody z zajęć\test\sumowanie.txt"))

#_________________________________________________________________
#Funkcja zliczająca znaki z plików w katalogu

import os

def letters_count_distinct(path):
    file_names = [os.path.join(path,name) for name in os.listdir(path)
                   if os.path.isfile(os.path.join(path,name))]
                    # Without the 'if', the code would be stuck on a folder
                    # (if any folders were included in the dir)
    counter = {}
    import string
    # string.ascii_lowercase = pre-initialized string used as string constant.
    # abcdefghijklmnopqrstuvwxyz
    # Code below creates a dictionary containing letters
    for letter in string.ascii_lowercase:
        counter[letter] = 0  

    for name in file_names:
        text = open(name).read()
        text = text.lower()
        
        for ch in text:
           if ch.isalpha():  # Check if the character is a letter
                if ch in counter:
                    counter[ch] += 1
                else:
                    counter[ch] = 1
        
    print_counter(counter)
        
        
def print_counter(counter):
    keys = list(counter.keys())
    keys.sort()
    for key in keys:
        print(f"{key}:\t{counter[key]:3}")

letters_count_distinct(r"C:\Users\krzys\Desktop\UE\Python\Kody z zajęć\test")
    
#_________________________________________________________________

# -*- coding: utf-8 -*-

#####
lan = "    Ala ma kota   "
#szukana = "a"
#if szukana in lan:
#    print(lan.index(szukana)) # szukana musi istnieić, inaczej będzie błąd

#####
#" ".join(...)

#####
#lista = lan.split() # dzieli lan wzflędem parametru (jesli nie ma, to biale znaki) zwraca listę elementow
#print(lista)
#
#lista = lan.split("a")
#print(lista)

#####
#print(lan.strip(),"|", sep="") # strip usunie białe znaki na początku i końcu rstrip tylko po prawej, lstrip tylko po lewej
#print(lan.lstrip(),"|", sep="")
#print(lan.rstrip(),"|", sep="")

#test= "dd"
#print(test)
#print(test.isalpha()) # czy ciąg test, to tylko litery
#print(test.isspace()) # czy ciąg test, to tylko białe znaki
#print(test.isdigit()) # czy ciąg test, to tylko cyfry
#
#test= "61"
#print(test)
#print(test.isalpha())
#print(test.isspace())
#print(test.isdigit())
#
#test= " \n\t"
#print(test)
#print(test.isalpha())
#print(test.isspace())
#print(test.isdigit())

#test = "Ala ma 21 kotów i 13 psów"
#print(test.islower())
#print(test.isupper())
#test = test.lower()
#
#print(test)
#test = test.upper()
#print(test)

####################
 #                  #
  #    Przykłady     #
   #                  #
    ####################

'''
Funkcja sumuje wszystkie cyfry zapisane w pliku i zwraca wartoć.
'''
def sum_digit(file_name):
    text = open(file_name).read() # try 'r' jest domylny. Wczytujemy cały plik do pamięci, jako tekst (string)
    s_digit = 0
    
    for char in text: # idziemy przez tekst znak po znaku
        if char.isdigit(): # if char.isdigit()==True:
            s_digit += int(char)
        
    return s_digit

def sum_digit2(file_name):
    text = open(file_name).read() # try 'r' jest domylny. Wczytujemy cały plik do pamięci, jako tekst (string)
    s_digit = 0
    
    for char in text: # idziemy przez tekst znak po znaku
        try:
            s_digit += int(char)
        except:
            pass
        
    return s_digit

#s = sum_digit2("xyz.txt")
#print(s)
    
'''
Funkcja sumuje wszystkie liczb zapisane w pliku (zakładamy, że nie stykają się one z innymi znakami niż białe i zwraca wartoć.
'''
# Funkcja dla całkowitych
def sum_numbers(file_name):
    text = open(file_name).read() # try 'r' jest domylny. Wczytujemy cały plik do pamięci, jako tekst (string)
    
    s_num = 0
    words = text.split()
    for word in words:
        if word.isdigit():
            s_num += int(word)
        
    return s_num

# Funkcja dla wszystkich liczb
def sum_numbers2(file_name):
    text = open(file_name).read() # try 'r' jest domylny. Wczytujemy cały plik do pamięci, jako tekst (string)
    
    s_num = 0
    words = text.split()
    for word in words:
        try:
            s_num += float(word)
        except:
            pass
        
    return s_num

#s = sum_numbers("xyz.txt")
#print(s)
#s = sum_numbers2("xyz.txt")
#print(s)

'''
Zadanie, w którym należy stworzyć funkcję -- jako parametr dostaje katalog.
Należy w katalogu policzyć liczbę wystąpień wszystkich liter (duże traktujemy jak małe).
I wywietlić.

Algorytm:
    1. Otworzyć folder i pobrać nazwy wszystkich plików (tylko plików).
    2. Stwórz słownik do liczenia
    3. Przejdź przez pliki i otwieraj kolejne pliki:
        3.1. Zamień wszystkie litery na małe.
        3.2. Przejdź przez każdy znak:
            3.2.1. Sprawdź czy litera, jesli tak, to:
                3.2.1.1. Sprawdź, czy istnieje w słowniku, jeli tak, to:
                    Zwiększ o 1.
                    Jesli nie, to:
                    Dodaj do słownika, jako 1 wystapienie.
    4. Wywietl słownik.
'''
def letters(path):
    # 1.
    # Zapisujemy w liscie nazwy plików ze sciezka, czyli os.path.join(path,name)
    file_names = [os.path.join(path,name) for name in os.listdir(path) 
                        if os.path.isfile(os.path.join(path,name))] # tylko, jesli sa plikami
    # 2.
    counter = {}
    #Gdybysmy chcieli wszystkie litry, to najpierw je dodajemy z 0:
    import string
    for letter in string.ascii_lowercase:
        counter[letter] = 0
    
    # 3.
    for name in file_names:
        text = open(name).read()
        # 3.1.
        text = text.lower()
        # 3.2.
        for ch in text:
            # 3.2.1.
            if ch.isalpha(): # sprawdzamy, czy litera
                # 3.2.1.1.
                if ch in counter:
                    counter[ch] += 1
                else:
                    counter[ch] = 1
                    
    print_counter(counter)


def print_counter(counter):
#    for key,val in zip(counter.keys(),counter.values()):
#        print(f"{key}:\t{val:3}")
    keys = list(counter.keys())
    keys.sort()
    for key in keys:
        print(f"{key}:\t{counter[key]:3}")
        
letters("test")


##### Przykład ZIP-a
#l = [1,2,5,67,1]
#l2 = ["Ala", 2, 5, 3.4]
#
#for el1, el2 in zip(l, l2):
#    print(el1,el2)
