# Napisz program, który pięcokrotnie wywołuje funkcję rekurencyjną.

def wiadomość(i):
    if i > 0:
        print('Wywołanie', i)
        wiadomość(i-1)

wiadomość(5)        