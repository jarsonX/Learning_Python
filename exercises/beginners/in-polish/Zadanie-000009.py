'''ZADANIE 9'''
# Napisać program, który dla podanej liczby całkowitej wyświetla jej dzielniki. 
# Przykładowo, dla liczby 21 dzielniki to: 1, 3, 7, 21.

'''ROZWIĄZANIE'''
# Przyjmuje liczbę całkowitą dodatnią od użytkownika
# Zabezpiecza przed wprowadzeniem wartosci innej niż dodatni int
def load_int(text):
    try:
        my_int = int(input(text))
    except ValueError:
        my_int = load_int("Błąd. Podaj liczbę całkowitą, aby poznać jej dzielniki: ")
    return my_int

# Znajduje dzielniki
def find_factors(var_x):
   var_x = abs(var_x)  # Zamieniamy na wartosć bezwględną, żeby ułatwić sprawę
   for i in range(1, var_x + 1):
       if var_x % i == 0:
           print(i, " ", end = "")
   
# Input
user_num = load_int("Podaj liczbę całkowitą: ")

# Output
if user_num == 0:
    print("Nie można dzielić przez zero, tak więc 0 nie może mieć dzielników.")
else:
    print("\nDzielniki liczby", abs(user_num), "to:")
    result = find_factors(user_num)
