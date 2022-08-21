# Napisz program, który dla x rosnącego od 0 do 5 z krokiem 0,5, oblicza wartość funkcji
# y = x^2 + 1. Rozwiąż to zadanie przekazując argument funkcji przez wartość.

def oblicz(a):
    return a * a + 1

krok = 0.5
x = 0

while x <= 5:
    y = oblicz(x)
    print(f'x = {x:.2f},', '\t', f'y = {y:.2f}.')
    x += krok