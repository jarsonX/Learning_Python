# Napisz program, który oblicza sumę wartości konkretnych elementów listy za
# pomocą rekurencji.

def suma_zakresu(lista, start, koniec):
    if start > koniec:
        return 0
    else:
        return lista[start] + suma_zakresu(lista, start + 1, koniec)

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(suma_zakresu(liczby, 3, 10))