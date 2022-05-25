'''ZADANIE 7'''
# Gra w ”Za dużo, za mało”. Komputer losuje liczbę z zakresu 1 . . . 100, a gracz
# (użytkownik) ma za zadanie odgadnąć, co to za liczba poprzez podawanie kolej-
# nych wartości. Jeżeli podana wartość jest:
#  większa – wyświetlany jest komunikat „Podałeś za dużą wartość”,
#  mniejsza – wyświetlany jest komunikat „Podałeś za małą wartość”,
#  identyczna z wylosowaną – wyświetlany jest komunikat „Gratulacje” i gra
# się kończy.

'''NOTATKI'''
# Zadanie było rozwiązywanie na zajęciach, ale poprawiłem kod, tzn. dodałem funkcję,
# która sprawia, że program nie wykrzacza się po podaniu błędnej wartosci.

'''ROZWIĄZANIE'''
import random
random_num = random.randint(1,100)

# Zabezpiecza przed podaniem wartosci innej niż int
def load_num(text):
    try:
        my_num = int(input(text))
    except ValueError:
        my_num = load_num("Błąd. Podaj liczbę całkowitą: ")
    return my_num

user_num = load_num("Podaj liczbę: ")
counter = 1

# Prosi o podanie wartosci dopóki użytkownik nie trafi
while user_num != random_num:
    if user_num > random_num:
        print("Za dużo.")
    else:
        print("Za mało.")
    user_num = load_num("Podaj liczbę: ")
    counter += 1
    
print("Gratulacje!")
print(f"Liczba prób: {counter}")