### Exercícios
#6. Usando o array criando no exercício 4, substitua todos os números ímpares com o valor -1 sem alterar o array original.
import numpy as np
a = np.random.randint(0,1001,50)
impar = np.where(a%2==0, a, -1)
print(a)
print(impar)