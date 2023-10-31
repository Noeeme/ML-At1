# Questão 1:
def primos() :
    numeros = []
    primo = []
    for numero in range(10) :
        numero = int(input("Digite um numero: "))
        if numero < 0:
            print("Número inválido. Digite apenas valores positivos")
        else :
            numeros.append(numero)
        
    for numero in numeros:
        if numero == 2:
            primo.append(numero)
        elif numero > 2 and numero % 2 != 0:
            is_primo = True
            for i in range(3, numero, 2):
                if numero % i == 0:
                    is_primo = False
                    break
            if is_primo:
                primo.append(numero)
    
    return primo

# Questão 2:
def elemento() :
    lista1 = []
    lista2 = []
    for i in range(5)  :
        i = int(input("Lista 1 - Digite um número: "))
        lista1.append(i)
    for i in range(5) : 
        i = int(input("Lista 2 - Digite um número: "))
        lista2.append(i)
    conj1 = set(lista1)
    conj2 = set(lista2)
    diferenca = conj1.difference(conj2), conj2.difference(conj1)
    return diferenca

# Questão 3:
def segundo_maior(l) : 
    return sorted(set(l), reverse = True)[1]

# Questão 4:
def ordenar_nome():
    lista = []
    for nome in range(5) :
        nome = str(input("Digite o nome: "))
        idade = int(input("Digite a idade: "))
        tupla = (nome, idade)
        lista.append(tupla)
    lista_ordenada = sorted(lista, key= lambda tupla: tupla[0])
    return lista_ordenada

# Questão 5:
lista = [5,2,8,18,9,7,4,3,6]

menor, maior = min(lista), max(lista)

# Questão 6:
## arquivo = pd.read_csv("arquivo.csv").head()

# Questão 7:
## arquivo["coluna"] == True

# Questão 8:
## - Preenchendo os valores ausentes :
### arquivo.fillna(valor, inplace = True)
## - Removendo os valores ausentes:
### arquivo.dropna(inplace = True)

# Questão 9:
import matplotlib.pyplot as plt 
import numpy as np 
fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), 
                        layout="constrained")

for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5), 
                               transform=axs[row, col].transAxes,
                               ha='center', va='center', fontsize=18,
                               color='darkgrey')

fig.suptitle('plt.subplots()')

# Questão 10:
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)