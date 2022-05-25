'''ZADANIE 2'''
# W sklepie ze sprzętem AGD oferowana jest sprzedaż ratalna. Napisz program
# umożliwiający wyliczenie wysokości miesięcznej raty za zakupiony sprzęt. Danymi
# wejściowymi dla programu są:
#  cena towaru (od 100 zł do 10 tyś. zł),
#  liczba rat (od 6 do 48).
# Kredyt jest oprocentowany w zależności od liczby rat:
#  od 6–12 wynosi 2.5% ,
#  od 13–24 wynosi 5%,
#  od 25–48 wynosi 10%.
# Obliczona miesięczna rata powinna zawierać również odsetki. Program powinien
# sprawdzać, czy podane dane mieszczą się w określonych powyżej zakresach, a w
# przypadku błędu pytać prosić użytkownika ponownie o podanie danych.

'''ROZWIĄZANIE'''
# Function
# Przyjmuje dane od użytkownika
# Zabezpiecza przed podaniem wartosci spoza okreslonych przedziałów
def load_data(from_min, to_max, name):
    data = int(input(f"{name} - podaj wartość: "))
    while not from_min <= data <= to_max:
        data = int(input(f"{name} - nieprawidłowy przedział. Podaj ponownie: "))
    return data

#Input
cena_towaru = load_data(100, 10000, "Cena towaru")
liczba_rat = load_data(6, 48, "Liczba rat")

if 6 <= liczba_rat <= 12:
    oprocentowanie = 0.025
elif liczba_rat <= 24:
    oprocentowanie = 0.05
else:
    oprocentowanie = 0.1

#Output
mies_rata = (cena_towaru + (cena_towaru * oprocentowanie)) / liczba_rat
oprocentowanie *= 100

print(f"\nPARAMETRY \n- Cena towaru: {cena_towaru:.2f} PLN\n- Liczba rat: {liczba_rat} \n- Oprocentowanie: {oprocentowanie}% \n- Miesięczna rata: {mies_rata:.2f} PLN")
