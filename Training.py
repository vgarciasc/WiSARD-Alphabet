import os
import BitmapReader

class Training(object):
    retinas = [[]]
    classifications = []

    def __init__(self, retinas, classifications):
        self.retinas = retinas
        self.classifications = classifications

def getTrainingFromDirectory(alphabet_qt):
    retinas = []
    classifications = []

    directory = "alphabet_training"
    files = os.listdir(directory)
    # print("Files found for training in directory '" + directory + "': " + str(files))

    for file in files:
        file_name_data = file.split("_")   
        class_name = file_name_data[0]
        alphabet_id = int(file_name_data[1].split(".")[0])
        if alphabet_qt != -1 and alphabet_id > alphabet_qt:
            continue
        
        imgArray = BitmapReader.getImageAsPixels(directory + "/" + file)
        if len(imgArray) > 0:
            retinas.append(imgArray)
            classifications.append(class_name)

    output = Training(retinas, classifications)
    return output