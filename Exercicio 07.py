### Exercícios
#7. Crie um array 1D com 100 valores de ponto flutuante (float), converta-o em uma matriz 2D com 10 linhas e 10 colunas.
import numpy as np
a = np.arange(0,100,dtype=float)
a = a.reshape(10,10)
print(a)
