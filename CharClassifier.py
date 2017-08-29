from PyWANN import WiSARD
import numpy as np
import BitmapReader
import Training
import pprint
import operator
import sys

num_bits_addr = 2
bleaching = True

w = WiSARD.WiSARD(
    num_bits_addr = num_bits_addr,
    bleaching = bleaching
)

args = sys.argv

if len(args) != 2:
    print("[ERROR]: Invalid format. Example: 'CharClassifier.py ./tests/test_a_1.png'")
    exit()
else:
    file_to_test = str(args[1])

print("=============")
print("Testing: " + file_to_test)
print("=============")

for i in range(1, 6):
    training = Training.getTrainingFromDirectory(i)
    w.fit(training.retinas, training.classifications)

    X_test = [BitmapReader.getImageAsPixels(file_to_test)]
    results = w.predict(X_test)

    #rank results
    dictionary = dict(zip(w.classes_, results[0]))
    classes_ranked = sorted(
        dictionary.items(),
        key = operator.itemgetter(1),
        reverse = True
    )

    #print top 3 classifications
    pprint.pprint(classes_ranked[0:3])

    for res in results:
        index = np.argmax(results)
        print(">> Alphabets: " + str(i))
        print("Predicted: " + str(w.classes_[index]) + "\n")