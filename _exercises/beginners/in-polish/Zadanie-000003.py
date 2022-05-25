'''ZADANIE 3'''
# Napisać program, który pobiera od użytkownika liczbę całkowitą dodatnią, a 
# następnie wyświetla na ekranie kolejno wszystkie liczby nieparzyste nie większe od
# podanej liczby. Przykład, dla 15 program powinien wyświetlić 1, 3, 5, 7, 9, 11, 13,
# 15

'''ROZWIĄZANIE'''
# Function
# Przyjmuje liczbę całkowitą od użytkownika
# Zabezpiecza przed wprowadzeniem wartosci innej niż dodatni int
def load_int(text):
    try:
        my_int = int(input(text))
    except ValueError:
        my_int = load_int("Błąd. Podaj liczbę całkowitą: ")
    while my_int < 0:
        my_int = load_int("Błąd. Podaj liczbę całkowitą dodatnią: ")
    return my_int

# Input
user_number = load_int("Podaj liczbę: ")

# Output
for num in range(user_number + 1):
    if num % 2 != 0:
        print(num, end = " ")
