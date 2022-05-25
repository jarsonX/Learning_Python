'''ZADANIE 8'''
# Napisać program, który pobiera od użytkownika liczbę całkowitą, a następnie:
# oblicza sumę cyfr tej liczby, stosunek średniej arytmetycznej cyfr 
# parzystych do średniej arytmetycznej cyfr nieparzystych.

'''NOTATKI'''
# /1/ Policz sumę cyfr                      --> zwróć w konsoli
# /2/ Policz srednią cyfr parzystych.
# /3/ Policz srednią cyfr nieparzystych.
# /4/ Policz stosunek (iloraz) (2) do (3)   --> zwróć w konsoli

# Podana liczba powinna być duża (tj. składać się z wielu znaków), żeby
# to w ogóle miało sens.

# Problem 1: program wykrzaczy się przy liczbach jednoznakowych.
# ---> Rozwiązanie w wierszu 65. Komunikat o tym, że nie można policzyć.
# Problem 2: użytkownik podaje liczbę ujemną. 
# ---> Rozwiązanie: nie widzę sensu podawania liczby ujemnej, więc 
# automatycznie zamieniamy na dodatnią + komunikat dla użytkownika.

'''ROZWIĄZANIE'''
# Functions
def load_num(text):  # input i error handling
    try:
        my_num = int(input(text))
    except ValueError:
        my_num = load_num("Błąd. Podaj liczbę całkowitą: ")
    if my_num < 0:
        my_num *= -1
        print("Podana liczba ujemna została zmieniona na dodatnią.")
    return my_num

def average(name_of_list):  # oblicza srednią
    if len(name_of_list) != 0:
        avg = sum(name_of_list) / len(name_of_list) 
        return avg
    else:
        pass  # Nie dzielimy przez 0.

# Input
user_num = load_num("Podaj liczbę całkowitą: ")
list_based_on_num = [int(x) for x in str(user_num)]  #Przerabia podaną liczbę
# na listę, na zasadzie 2350 -> [2, 3, 5, 0]

# Cyfry parzyste i nieparzyste / tworzy listy
list_even = []
list_odd = []

for x in list_based_on_num:
    if x % 2 == 0:
        list_even.append(x)  # jesli parzysta
    else:
        list_odd.append(x)  # jesli nieparzysta

# Rezultaty
print("\nREZULTATY")
print("Suma cyfr wynosi: ", sum(list_based_on_num))  # /1/

if sum(list_odd) > 0:  # error handling: dzielenie przez 0, gdy liczba nie zawiera cyfr nieparzystych
    try:
        print("Stosunek średnich arytmetycznych wynosi: ", average(list_even) / average(list_odd))
    except TypeError:
        print("Stosunek średnich równy jest 0, ponieważ podana liczba nie zawiera cyfr parzystych.")
else:
    print("Policzenie stosunku średnich jest niemożliwe.")