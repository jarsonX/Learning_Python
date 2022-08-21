# Napisz program, który rekurencyjnie znajduje 10 pierwszych liczb trójkątnych
# i wyświetla je na ekranie komputera.

def trójkąt(n):
    if n == 1:
        return 1
    else:
        return n + trójkąt(n-1)

for i in range(1, 11):
    print('#', i, ' ', trójkąt(i), sep='')