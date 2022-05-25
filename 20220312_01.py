#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Komentarz w jednej linii

'''
Komentarz
w
wielu
liniach :)
'''

########################################
#                                      #
#     Instrukcje wyjcia (podstawy)     #
#                                      #
########################################

print("Witaj Świecie") # Domyślnie na końcu robi nową linię
print("Witaj Świecie", end="") # możemy to zmienić, modyfikując end
print("test")
print("test","test2","kolejna wartość") # możemy wyświetlać kilka elementów, po przecinku

########################################
#                                      #
#            Zmienne i typy            #
#                                      #
########################################

# Zmienna ma nazwę (my ją nadajemy) i typ (autmatycznie)
zmienna = 54

"""
Konieczność:
    zaczynają się od litery
    składają się tylko z liter, cyfr i znaku _
Zwyczaj: 
    zmienne zaczynają się małymi literami
    notacja wielbłądzia liczbaPierwsza (C/JAVA/C#)
    notacja wężowa liczba_pierwsza (Python)
Uwaga:
    Należy uważać, aby nie zastąpić nazw funkcji itp.
"""

####################
#       Typy       #
####################

# Mówią nam, jaki jest zakres watrtości zmiennej

# Typy "proste"
# int -- liczby całkowite "nieskończony"
a = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# float -- liczba rzeczywista (zmiennopozycyjna)
b = 3.14
# bool -- boolowski True albo False
c = True
d = -123

print(a,b,c,d)

# Typy złożone
# str -- strint (łańcuch znaków)
s = "Ala ma kota"
print(s)
# complex -- liczby zespolone

####################
#  Rzutowanie      #
#       Konwersja  #
####################

# zmienna_typu1=typ1(zmienna_typu2) -- zmieniamy zmienna_typ2 na typ1 i zwracamy dp zmienna_typu1
zmienna_i = 15
zmienna_f = float(zmienna_i)

b = 3.99
b_i = int(b) # Utnie to, co po kropce (przecinku, separatorze)

s = "123"
s_i = int(s) # to zadziała tylko, jeśli w s są same cyfry

########################################
#                                      #
#          Instrukcja wejscia          #
#                                      #
########################################

zmienna = input("Opcjonalny tekst") # Zawsze zwraca str
# Jeśli chcemy, aby zmienić typ, to trzeba dokonać konwersji
zmienna = int(zmienna) # Dokonujemy konwersji na int 

# W skrócie, można to napisać tak:
zmienna = int(input("Opcjonalny tekst"))
    
# Przykład z dodawaniem
print("Dodawnie dwóch liczb")
liczba1 = int(input("Podaj pierwszą liczbę "))
liczba2 = int(input("Podaj drugą liczbę "))

suma = liczba1 + liczba2

print("Suma liczb",liczba1,"i",liczba2,"wynosi",suma)

########################################
#                                      #
#  Instrukcje wyjcia (różne warianty)  #
#                                      #
########################################

imie = "Ala" # input("Podaj swoje imię: ")
waga = 67.562 #float(input("Podaj swoją wagę: "))
wzrost = 173 #int(input("Podaj swoją wzrost: ")) # zmodyfikujemy

print(imie,"waży",waga,"kg i ma",wzrost,"cm wzrostu")
# Wersja, jak w JAVA
print("%s waży %.3f kg i ma %d cm wzrostu" % (imie,waga,wzrost)) 
# %s -- łańcuch znaków
# %f -- liczba rzeczywista, możemy ograniczać, np.
#       %.2f -- do drugiego miejsca po przecinku
#       %5.2f -- na 5 pozycjach, z czego 2 po przecinku
# %d -- decimal, czyli liczby całkowite
# Wersja, jak z C#
print("{} waży {:.3f} kg i ma {} cm wzrostu".format(imie,waga,wzrost)) 
# {:.3f} -- jeśli wiemy, ze liczba i chcemy ją zapisać do 3 miejsca po przecinku

print("{0} waży {1:.3f} kg i ma {2} cm wzrostu, więc {0} waży poprawnie".format(imie,waga,wzrost)) 
# format(waga,imie,wzrost) to determinuje indeksy w kolejności od 0:
#    0 imie
#    1 waga
#    2 wzrost
# {1} -- wstaw w to miejsce element o indeksie 1

# Zapis, w którym poprzedzamy ciąg literką f. to znaczy, że tekst będzie formatowany
print(f"{imie} waży {waga:.3f} kg i ma {wzrost} cm wzrostu") 
# {waga:.3f} -- :.3f, to informacja, żeby tę liczbę typu float (to f oznacza float) wyświetlić na 3 miejscach po przecinku
# {waga:5.3f} -- :.3f, to informacja, żeby tę liczbę typu float (to f oznacza float) wyświetlić na 5 miejscach z czego 3 miejscach po przecinku

# Wyrównanie wyświetlanych liczb do separatora (przecinka, kropki)
# Wyświetlamy liczby na 8 znakach, z czego 2 po przecinku
print("%8.2f" % (3.156))
print("%8.2f" % (234.22))
print("%8.2f" % (1.232323232323))
print("%8.2f" % (9.999999999999))
print("%8.2f" % (99.9))
print("%8.2f" % (3242.443344))

########################################
#                                      #
#              Operatory               #
#                                      #
########################################
####################
#   Przypiasania   #
####################
"""
=
L = P
Zawsze wykonuje wszystko co jest w P i następnie wynik wpisuje do L
a = 5 # przypisuje 5 do a
b = 6
c = 3
s = a+b+c # doda a do b i do c, a wynik wpisze do s, czyli 14
"""

####################
#   Arytmetyczne   #
####################
"""
+, -, * (dodawnie, odejmowanie, mnożenie)
// -- dzielenie całkowite
/ -- dzielenie rzeczywiste
"""
a = 5
b = 2
print(a/b) # 2.5
print(a//b) # 2
print(7/5) # 1.4 
print(7//5) # 1
"""
% -- dzielenie modulo, czyli reszta z dzielenia
"""
print(a%b) # 1
print(7%5) # 2
print(7%4) # 3
"""
** -- potęga
"""
print(a**b)
print(b**a)

# możliwośc skrótu, czyli dla:
a = 11
b = 23
# zamiast:
a = a + b
# można napisać:
a += b

# To działą dla wszystkich operatorów

####################
#     Logiczne     #
####################
"""
and -- logiczne "i", && -- JAVA/C, & -- C#
or -- logiczne "lub", || -- JAVA/C, | -- C#
not -- logiczna negacja, ! -- JAVA/C/C#
"""

####################
#    Porównania    #
####################
"""
> większ
< mniejszy 
>= większy lub równy
<= mniejszy lub równy
== równy
!= różny
"""
