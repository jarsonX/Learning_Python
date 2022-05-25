########################################
#                                      #
#           Wstęp do funkcji           #
#                                      #
########################################

# Funkcje, to takie podprogramy, dzięku którym można "wykonywać" mniejsze zadania.
# * Stosujemy dla podzielenia problemu na podproblemy.
# * Stosujemy dla mniejszenia redundancji (pisania tego samego kodu).
# * Stosujemy dla czytelności.

#def -- informacja, że definiujemy nową funkcję
#def nazwa_funkcji(parametry): # parametry opcjonalnie
#    ciało_funkcji
#    ciało_funkcji
#    ciało_funkcji
#    ciało_funkcji
#    return zwracany_wynik # return opcjonalnie

# Przykładwowa funkcja do wczytania danych
def wczytaj_raty():
    rata = int(input("Podaj liczbę rat: "))
    while rata < 6 or rata >48:
        rata = int(input("Podałaś / Podałeś złą liczbę rat, podaj nową liczbę: "))
    return rata # zwraca liczbę rat

def wczytaj_dane(od, do, nazwa): #od, to dla mnie dolna granica liczby; do, to górna granica liczby; nazwa, to łańcuch znaków informujący, co wpisujem
    liczba = int(input(f"Podaj {nazwa}: "))
    while liczba < od or liczba >do:
        liczba = int(input(f"Podałaś / Podałeś złą {nazwa}, podaj nową wartość: "))
    return liczba

def wczytaj_liczbe(tekst): # funkcja, która ma wczytać int i tylko int
    try: # rozpoczynamy obsługę wyjątku -- jesli chcemy wyłapać jakiś możliwy błąd
        liczba = int(input(tekst))
    except ValueError:
        liczba = wczytaj_liczbe("Podałaś / Podałeś złą wartość, spróbuj jeszcze raz ")
    return liczba

def wczytaj_dane2(od, do, nazwa):
    liczba = wczytaj_liczbe(f"Podaj {nazwa}: ")
    while liczba < od or liczba >do:
        liczba = wczytaj_liczbe(f"Podałaś / Podałeś złą {nazwa}, podaj nową wartość: ")
    return liczba

# r = wczytaj_raty()
# print(r)

# r = wczytaj_dane(6,48,"liczbę rat")
# print(r)
# r = wczytaj_dane(100,10000,"cenę")
# print(r)

# r = wczytaj_dane2(1,5,"testową liczbę")
# print(r)

def stopnie_C_na_F(st_C):
    st_F = 32 + 1.8 * st_C
    return st_F

# from random import randint
# for _ in range(10):
#     st_C = randint(-30,40)
#     st_F = stopnie_C_na_F(st_C)
#     print(f"Mamy dzisiaj {st_C:.1f} stopni C, czyli {st_F:.1f} stopni F")

########################################
#                                      #
#                Listy                 #
#                                      #
########################################

# Lista, to taka "zmienna", która ma wiele ("nieskończenie") pudełek, a nie tylko jedno.

# a = 5

# l = [7,1,4]

# #nazwa_listy[indeks_elementy] -- aby dodstać się do elementu listy
# print(l[0]) # element pierwszy w liście ma indeks 0
# print(l[2]) # w tym przypadku lista ma 3 elementy, więc ostatni ma indeks 2
# print(l[-1]) # zawsze możemy wpisać -1 jako indeks i jest to ostatni (analogicznie -2, -3 itd.)

# #Funkcje wbudowane w język (nie dotyczą tylko list, ale też innych struktur)
# #len(lista) -- długość listy
# #sum(lista) -- suma elementów (tylko dla liczbę)
# #min(lista) -- minimalna liczba
# #max(lista) -- maksymalna liczba

# print(len(l))
# print(sum(l))
# print(min(l))
# print(max(l))

# l = [1,3.14,"Ale", "Ala ma kota",43367]
# print(l)

# # Dwa sposoby "przejścia" przez listę
# # odczytanie całego elementu -- nie możemy zmienić jego wartości
# for el in l:
#     print(el)
#     el*=2
#     print(el)
# print(l)

# # odczytanie indeksów elementu -- możemy "wszystko"
# # len(l) -- liczba elementów listy
# # indeksujemy od 0
# # indeksy mają wartość [0, len(l)-1]

# for i in range(len(l)):
#     print(l[i])
#     l[i]*=2
#     print(l[i])
# print(l)

def suma(lista):
    wynik = 0
    for el in lista:
        try:
            wynik += el
        except TypeError:
            pass # pass w Pythonie, to "nic nie rób"
    return wynik

# l = [1,3.14,"Ale", "Ala ma kota",43367]
# # print(sum(l))

# print(suma(l))

# lista = [2**x for x in range(10)]
# print(lista)
# lista = [0 for x in range(5)]
# print(lista)

# from random import randint
# lista = [randint(0,10) for x in range(20)]
# print(lista)

# # Do listy można też dodawać nowe elementy
# l = [34, 2, "Test"]
# print(l)
# l.append("Asia i Ola")
# print(l)

# Listy wielowymiarowe, to takie listy, które składają się z list

l2w = [[1,2,3],[4,3,3]]
l2w[0][2]=99

# # Przejście przez listę 2 wymiarową, wersja z indeksami
# # Przejście przez wiersze:
# for w in range(len(l2w)):
#     #Przejście przez kolumny:
#     for k in range(len(l2w[w])):
#         print(l2w[w][k]) # -- każdy element z listy
        
def wyswietl(lista):
    for w in range(len(lista)): # ta pętla idzie przez kolejne wiersze
        for k in range(len(lista[w])): # a ta przez wszystkie kolumny w każdym wierszu
            #print(lista[w][k],end=" ") 
            print(f"{lista[w][k]:5}",end=" ") 
        print() # zrób nową linię na końcu wiersza

#wyswietl(l2w)

"""
stworzy listę list (macierz) 5 x 5 liczb całkowitych wylosowanych z zakresu
{−5, −4, . . . , 5},
"""
from random import randint
# #Długi sposób
# lista5x5 = []
# for _ in range(5):
#     lista = [randint(-5,5) for _ in range(5)]
#     lista5x5.append(lista)
#print(lista5x5)

# Krótki sposób
lista5x5 = [[randint(-5,5) for _ in range(5)] for _ in range(5)]
wyswietl(lista5x5)




