### Exercícios
#5. Usando o array criando no exercício anterior, substitua todos os números ímpares maiores que 50 por -1 no array original.
import numpy as np
a = np.random.randint(0,1001,50)
a[(a%2!=0)&(a>50)]=-1
print(a)