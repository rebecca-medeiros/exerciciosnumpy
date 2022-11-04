### Exercícios
#11. A partir dos dados lidos na matriz iris_2d, filtre as linhas que possuem (coluna 3) > 1.5 e (coluna 1) < 5.0.
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter = ",", dtype = 'float', usecols=[0,1,2,3])
x = (iris_2d[:, 3] > 1.5) & (iris_2d[:, 1] < 5.0)
print(iris_2d[x])