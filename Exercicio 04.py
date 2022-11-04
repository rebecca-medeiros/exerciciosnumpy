### Exercícios
#4. Crie um array 1D como números inteiros (50 elementos) de 0 a 1000 e extraia apenas os números pares. Imprima o resultado.
import numpy as np
a = np.random.randint(0,1001,50)
par = a[a%2==0]
print(par)