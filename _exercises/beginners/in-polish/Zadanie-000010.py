'''ZADANIE 9'''
# Napisać program, który sprawdza, czy podana liczba całkowita n, n > 1, jest
# liczbą pierwszą.

'''ROZWIĄZANIE'''
# Przyjmuje input w postaci int
def load_int(text):
    try:
        my_int = int(input(text))
    except ValueError:
        my_int = load_int("Błąd. Podaj liczbę całkowitą:")
    return my_int

user_num = load_int("Podaj liczbę całkowitą: ")

flag = False

if user_num > 1:
    for i in range(2, user_num):
        if (user_num % i) == 0:
            flag = True
            break  #  kończy pętlę

if flag:
    print(user_num, "nie jest liczbą pierwszą.")
else:
    print(user_num, "jest liczbą pierwszą.")
