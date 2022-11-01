
import numpy as np

print(np.__version__)

"""2. Crie um *array* 1D com números de 0 a 9 e imprima o resultado."""

a = np.arange(10)
print(a)

"""3. Crie uma matriz **booleana** de 3x3 e preencha os seus valores com 'True'. Imprima o resultado.

**Dica:** Verifique o uso da função **full** na documentação do [numpy](https://numpy.org/doc/stable/user/whatisnumpy.html).
"""

arr = np.full((3, 3), True)
print(arr)

"""4. Crie um *array* 1D como números inteiros (50 elementos) de 0 a 1000 e **extraia** apenas os números pares. Imprima o resultado."""

aint = np.random.randint(0,1001,50)
print(aint)
par = aint[aint%2==0]
print(par)
print(aint)

"""5. Usando o *array* criando no exercício anterior, **substitua** todos os números ímpares maiores que 50 por -1 no *array* original. """

arr = np.where((aint%2==0)&(aint>50), aint,-1) #(condicao, true, false)
arr

"""6. Usando o *array* criando no exercício 4, **substitua** todos os números ímpares com o valor -1 **sem** alterar o *array* original."""

i = np.where(aint%2==0, aint,-1)
print(i)
aint

"""7. Crie um *array* 1D com 100 valores de ponto flutuante (**float**), converta-o em uma matriz 2D com 10 linhas e 10 colunas."""

arr = np.random.rand(100)
matriz = arr.reshape(10,10)
matriz

"""8. Crie duas matrizes 2D de inteiros aleatórios (de 0 a 100) com dimensões 10x10. **Empilhe-as horizontalmente**.

**Dica:** verique as funções **hstack** e **concatenate** na documentação do [numpy](https://numpy.org/doc/stable/user/whatisnumpy.html)
"""

m1 = np.random.randint(0,101,(10,10))
m2 = np.random.randint(0,101,(10,10))

print(np.concatenate((m1,m2), axis=1))
print(f'com hstack:\n {np.hstack((m1,m2))}')

"""9. Crie duas matrizes 2D de inteiros aleatórios (de 0 a 100) com dimensões 10x10. **Empilhe-as verticalmente**.

Dica: verique as funções **vstack** e **concatenate** na documentação do [numpy](https://numpy.org/doc/stable/user/whatisnumpy.html)

"""

print(np.concatenate((m1,m2), axis=0))

print(f'com vstack:\n {np.vstack((m1,m2))}')

"""Para ler arquivos em formato *txt* que estão em formato de "tabelas", podemos usar a função **genfromtxt()** do **numpy**. Esta função recebe como argumentos: **caminho do arquivo txt** (path local ou uma url); **delimiter** para separar cada valor seguindo algum critério; **dtype** para converter os valores recebidos em algum tipo de dado conhecido (exemplo: **float**) e; **usecols** em que é definido o cabeçalho das colunas lidas a partir do arquivo. 
<br>
<br>
Vejamos um exemplo de uso da função **genfromtxt** sobre a base de dados 
<a href="https://archive.ics.uci.edu/ml/datasets/iris">Iris</a>.
"""

import numpy as np
# Caminho da base de dados é uma url disponível na internet (visite o link abaixo
# pelo navegador para título de curiosidade :))
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Lê os dados a partir do caminho passado e armazena em uma matriz 2D chamada iris_2d
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

# matriz 2D criada com os dados da base Iris
iris_2d

"""11. A partir dos dados lidos na matriz iris_2d, filtre as linhas que possuem (coluna 3) > 1.5 e (coluna 1) < 5.0."""



"""12. A partir dos dados lidos na matriz iris_2d, calcule a **média** e **desvio padrão** de cada coluna presente nos dados. Imprima o resultado."""



"""13. Crie um repositório no Github e versione todos os códigos que desenvolveram nesta lista de exercícios."""

