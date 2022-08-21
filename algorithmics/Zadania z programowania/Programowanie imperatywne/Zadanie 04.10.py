# Napisz program, który rekurencyjnie oblicza wartość n! dla n = 10.

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)

print(silnia(5))    