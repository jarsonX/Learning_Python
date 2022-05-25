'''ZADANIE 4'''
# Napisać program, który wczytuje od użytkownika liczbę całkowitą dodatnią n, a
# następnie wyświetla na ekranie wszystkie potęgi liczby 2 nie większe, niż podana
# liczba. Przykładowo, dla liczby 71 program powinien wyświetlić:
# 1
# 2
# 4
# 8
# 16
# 32
# 64

'''ROZWIĄZANIE'''
# Function
# Przyjmuje liczbę całkowitą dodatnią od użytkownika
# Zabezpiecza przed wprowadzeniem wartosci innej niż dodatni int
def load_int(text):
    try:
        my_int = int(input(text))
    except ValueError:
        my_int = load_int("Błąd. Podaj liczbę całkowitą: ")
    while my_int < 0:
        my_int = load_int("Błąd. Podaj liczbę całkowitą DODATNIĄ: ")
    return my_int

# Input
user_number = load_int("Podaj liczbę: ")
expo = 0  # wykładnik potęgi
base = 2 ** expo  # podstawa potęgi

#Output
while base * 2 < user_number:  # number * 2, żeby uwzględnić następną potęgę i nie liczyć jej w pętli
     base = 2 ** expo
     print(base, end = " ")
     expo += 1