### Exercícios
#9. Crie duas matrizes 2D de inteiros aleatórios (de 0 a 100) com dimensões 10x10. Empilhe-as verticalmente.
import numpy as np
m1 = np.random.randint(0, 101, (10,10))
m2 = np.random.randint(0, 101, (10,10))
print(f'Resposta usando concatenate:\n {np.concatenate((m1,m2),axis=0)}')
print("\n", "-"*20, "\n")
print(f'Resposta usando vstack:\n {np.vstack((m1,m2))}')