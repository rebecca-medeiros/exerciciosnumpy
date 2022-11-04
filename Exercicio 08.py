### Exercícios
#8. Crie duas matrizes 2D de inteiros aleatórios (de 0 a 100) com dimensões 10x10. Empilhe-as horizontalmente.
import numpy as np
m1 = np.random.randint(0, 101, (10,10))
print("\n", "-"*20, "\n")
m2 = np.random.randint(0, 101, (10,10))
print(f'Resposta usando concatenate: {np.concatenate((m1,m2),axis=1)}')
print(f'Resposta usando hstack: {np.hstack((m1,m2))}')