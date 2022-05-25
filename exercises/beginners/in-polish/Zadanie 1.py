'''ZADANIE 1'''
# Napisać program, który oblicza wartość współczynnika BMI (ang. body mass
# index) wg. wzoru: waga / wzrost^2. Jeżeli wynik jest w przedziale (18,5 - 24,9), to wypisuje
# ”waga prawidłowa”, jeżeli poniżej to ”niedowaga”, jeżeli powyżej ”nadwaga”.

# Dodatkowo program powinien informować o tym o ile należy zmienić wagę, aby BMI było prawidłowe.

'''ROZWIĄZANIE'''
waga = round(float(input("Podaj wagę: ")), 2)
wzrost = round(float(input("Podaj wzrost: ")), 2)
if wzrost > 3:
    wzrost /= 100

bmi = round(waga / wzrost ** 2, 1)

if 18.5 <= bmi <= 24.9:
    rezultat = "waga prawidłowa."
elif bmi > 24.9:
    rezultat = "nadwaga."
else:
    rezultat = "niedowaga."

print(f"\nPrzy wadze {waga} kg i wzroscie {wzrost} cm, Twoje BMI wynosi {bmi}. Rezultat: {rezultat}")

waga_poczatkowa = waga

while bmi >= 25 or bmi < 18.5:
    if bmi >= 25:
        waga -= 1
    else:
        waga += 1
    bmi = round(waga / wzrost ** 2, 1)

zmiana = waga_poczatkowa - waga
if zmiana > 0:
    print(f"\nDo poprawnego BMI należy zmniejszyć wagę o {zmiana} kg.")
elif zmiana < 0:
    print(f"\nDo poprawnego BMI należy zwiększyć wagę o {abs(zmiana)} kg.")
