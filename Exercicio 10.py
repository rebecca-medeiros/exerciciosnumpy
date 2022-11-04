### Exercícios
#10. Crie uma matriz 2D a partir dos dados da base Iris.
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter = ",", dtype = 'float', usecols=[0,1,2,3])
print(iris_2d)