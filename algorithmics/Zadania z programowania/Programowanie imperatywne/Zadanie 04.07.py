#Napisz program, który sortuje N liczb znajdujących się na liście.

# PSEUDOKOD
# Lista = pełen zakres
# Przejdź przez listę
    # Dla każdego n w zakresie:
        # Jeśli n > n+1:
            # Zamień miejscami n i n+1
        # (Jeśli nie, to przejdź do kolejnego j i sprawdź)
# Lista = pełen zakres - ostatnia liczba
    # powtórz resztę

# Na końcu każdej zewnętrznej pętli, ostatnia liczba jest posortowana.

def sortowanie(liczby):
    for i in range(len(liczby)-1, 0, -1):
        #print('OUTER LOOP', i, '\t', liczby, 'range:', range(i), '\n', '________________'*3)
        for j in range(i):
            #print('----inner loop', j, liczby)
            #print('Czy', liczby[j], '>', liczby[j+1], '?')
            #print('')
            if liczby[j] > liczby[j+1]:
                liczby[j], liczby[j+1] = liczby[j+1], liczby[j]

lista = [9, 6, 3, 8, 2, 1]

sortowanie(lista)

print(lista)        