import numpy as np

def read(filename):
    h = open("{}".format(filename), "r")
    for line in h:
        datal = line.split()
    data = np.array(datal)
    data = data.astype(int)
    h.close()
    return data
    

