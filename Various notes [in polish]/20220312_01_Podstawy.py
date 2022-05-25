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
print("%s waży %.3f kg i ma %d cm wzrostu" % (imie,waga,wzrost)) 
# %s -- łańcuch znaków
# %f -- liczba rzeczywista, możemy ograniczać, np.
#       %.2f -- do drugiego miejsca po przecinku
#       %5.2f -- na 5 pozycjach, z czego 2 po przecinku
# %d -- decimal, czyli liczby całkowite
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


