import pickle
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

roter1 = list(alphabet)
random.shuffle(roter1)
roter1 = ''.join(roter1)

roter2 = list(alphabet)
random.shuffle(roter2)
roter2 = ''.join(roter2)

roter3 = list(alphabet)
random.shuffle(roter3)
roter3 = ''.join(roter3)

f = open('roters.enigma', 'wb')
pickle.dump((roter1, roter2, roter3), f)
f.close()