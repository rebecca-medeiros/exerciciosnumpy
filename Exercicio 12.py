### Exercícios
#12. A partir dos dados lidos na matriz iris_2d, calcule a média e desvio padrão de cada coluna presente nos dados. Imprima o resultado.
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter = ",", dtype = 'float', usecols=[0,1,2,3])
print(f'-----\nMédia coluna 0: {np.mean(iris_2d[:,0])}\nDesvio padrão coluna 0: {np.std(iris_2d[:,0])}\n-----')
print(f'Média coluna 1: {np.mean(iris_2d[:,1])}\nDesvio padrão coluna 0: {np.std(iris_2d[:,1])}\n-----')
print(f'Média coluna 2: {np.mean(iris_2d[:,2])}\nDesvio padrão coluna 0: {np.std(iris_2d[:,2])}\n-----')
print(f'Média coluna 3: {np.mean(iris_2d[:,3])}\nDesvio padrão coluna 0: {np.std(iris_2d[:,3])}\n-----')