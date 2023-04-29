import numpy as np
print("Матричное умножение")
# скаляры
A = 2
B = 3

print(np.dot(A, B), '\n')

# вектор и скаляр
A = np.array([2., 3., 4.])
B = 3

print(np.dot(A, B), '\n')

# вектора
A = np.array([2., 3., 4.])
B = np.array([-2., 1., -1.])

print(np.dot(A, B), '\n')

# тензор и скаляр
A = np.array([[2., 3., 4.], [5., 6., 7.]])
B = 2

print(np.dot(A, B), '\n')
print("Создание массива")
B = np.ones((3, 2), 'complex')
print(B)
print("Доступ к элементам, срезы")
A = np.array([[1, 2, 3], [4, 5, 6]])

I1 = np.array([[False, False, True], [True, False, True]])
I2 = np.array([[False, True, False], [False, False, True]])

B = A.copy()
C = A.copy()
D = A.copy()

B[np.logical_and(I1, I2)] = 0
C[np.logical_or(I1, I2)] = 0
D[np.logical_not(I1)] = 0

print('B\n', B)
print('\nC\n', C)
print('\nD\n', D)

print("Форма массива и ее изменение")
A = np.arange(24)
B = A.reshape(4, 6)
C = A.reshape(4, 3, 2)
print('B\n', B)
print('\nC\n', C)

print("Перестановка осей и траспонирование")
A = np.array([[1, 2, 3], [4, 5, 6]])
print('A\n', A)
print('\nA data\n', A.ravel())

B = A.T
print('\nB\n', B)
print('\nB data\n', B.ravel())

print("Объединение массивов")
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
B = A[::-1]
C = A[:, ::-1]

D = np.stack((A, B, C))
print(D.shape)


print("Клонирование данных")
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.repeat(A, 2))

print("Математические операции над элементами массива")
A = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
B = np.exp(A)
C = np.log(B)

print('A', A, '\n')
print('B', B, '\n')
print('C', C, '\n')


print("Агрегаторы")
A = np.ones((10, 4, 5))

print('sum\n', A.sum((0, 2)), '\n')
print('min\n', A.min((0, 2)), '\n')
print('max\n', A.max((0, 2)), '\n')
print('mean\n', A.mean((0, 2)), '\n')

