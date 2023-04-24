import numpy
import numpy as np
import pandas as pd

array_unidim = np.array([1,2,3,4])

array_bidim = np.array([[1,2,3], [4,5,6]])

print(array_bidim.shape, array_bidim.ndim, array_bidim.dtype, array_bidim.size, type(array_bidim))

datos = pd.DataFrame(array_bidim)

print(datos)

unos = np.ones((4,3))
print(unos)
ceros = np.zeros((2,4,3))
print(ceros)

array_2 = np.random.randint(0,10,(2,5))

print(array_2)