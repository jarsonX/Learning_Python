import pandas
import random

lista = []
lista_double = []
lista_boolean = []
lista_decision = []

for i in range(100):
    lista.append(random.randint(0, 10))
    lista_double.append(random.random())
    lista_boolean.append(random.choice([True,False]))
    lista_decision.append(random.choice(['BUY','SELL','WAIT']))
    
data = pandas.DataFrame(lista)
data.set_axis(['Column 1'], axis=1, inplace=True)
data['Column 2'] = lista_double
data['Column 3'] = lista_boolean
data['Decision'] = lista_decision

#By default, pandas won't print the entire DF to consol, so let's change that:
pandas.set_option("display.max_rows", None, "display.max_columns", None) 

print(data)


