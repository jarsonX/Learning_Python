'''ZADANIE 6'''
# Napisać program, który pobiera od użytkownika ciąg liczb całkowitych. Pobieranie
# danych kończone jest podaniem wartości 0 (nie wliczana do danych). W następ-
# nej kolejności program powinien wyświetlić sumę największej oraz najmniejszej z
# podanych liczb oraz ich średnią arytmetyczną.
# 
# Przykład:
# Użytkownik podał ciąg: 1, -4, 2, 17, 0.
# Wynik programu:
# 13 // suma min. i maks.
# 6.5 // średnia

'''ROZWIĄZANIE'''
# Function
# Zabezpiecza przed wprowadzeniem wartosci innej niż liczba całkowita
# Tworzy listę
def load_num(text):
    try:
        my_num = int(input(text))
    except ValueError:
        my_num = load_num("Błąd. Podaj liczbę całkowitą: ")
    return user_list.append(my_num)  #Nie ma potrzeby definiowania parametru
# dla listy, bo używamy tylko jednej (więc okreslamy ją z góry).

# Inputy i zmienne
user_list = []
user_num = load_num("Podaj liczbę: ")

# Wykonuje funkcję dopóki użytkownik nie poda 0
while not (0 in user_list):
    user_num = load_num("Podaj liczbę: ")

# Oczyszcza listę z niepoprawnych wartosci i usuwa 0
while None in user_list:
    user_list.remove(None)

user_list.remove(0)

print()  # dodaje odstęp

# Output 
user_sum = min(user_list) + max(user_list)
print(f"{user_sum:5} // suma min. i maks.")

user_avg = user_sum / 2
print(f"{user_avg:5} // średnia")