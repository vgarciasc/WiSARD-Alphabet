from PyWANN import WiSARD
import numpy as np

retina_length = 64
num_bits_addr = 2
bleaching = False

w = WiSARD.WiSARD(
    num_bits_addr = num_bits_addr,
    bleaching = bleaching
)

X = [ [0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 1, 0, 0],
       [0, 0, 1, 0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 0, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 1]]

Y = ['class_a','class_a','class_b','class_b','class_a','class_a','class_b','class_a',]

w.fit(X, Y)

X_test = [[0, 0, 1, 1, 0, 0, 1, 0]]
result = w.predict(X_test)

print(result)