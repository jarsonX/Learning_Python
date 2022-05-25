'''ZADANIE 5'''
# Napisać program, który wczytuje liczby podawane przez użytkownika dotąd, do-
# póki nie podana zostanie liczba 0. Następnie wyświetlić sumę wszystkich poda-
# nych liczb.

'''ROZWIĄZANIE'''
# Function
# Zabezpiecza przed wprowadzeniem wartosci innej niż float
def load_num(text):
    try:
        my_num = float(input(text))
    except ValueError:
        my_num = load_num("Błąd. Podaj liczbę całkowitą: ")
    return my_num

# Input
user_number = load_num("Podaj liczbę: ")
result = 0

while user_number != 0:
    result += user_number
    user_number = load_num("Podaj kolejną liczbę: ")

# Output
print("\nTo już koniec. Suma podanych liczb wynosi " + str(result) + ".")
