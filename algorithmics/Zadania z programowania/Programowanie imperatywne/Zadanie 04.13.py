# Napisz program, który rekurencyjnie wyznacza największy wspólny dzielnik (NWD)
# dwóch liczb dodatnich x i y. 

# Jeśli x można podzielić bez reszty przez y, to NWD = y.
# Inaczej NWD(x, y) = NWD(x, reszta z dzielenia x/y)

def NWD(x, y):
    if x % y == 0:
        return y
    else:
        return NWD(x, x % y)

print(NWD(49, 28))