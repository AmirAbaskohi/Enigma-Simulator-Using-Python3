import pickle

alphabet = 'abcdefghijklmnopqrstuvwxyz'

f = open('roters.enigma', 'rb')
roter1, roter2, roter3 = pickle.load(f)
f.close()

def reflector(character):
	return alphabet[len(alphabet) - alphabet.find(character) - 1]

def codeCharacter(character):
	char1 = roter1[alphabet.find(character)]
	char2 = roter2[alphabet.find(char1)]
	char3 = roter3[alphabet.find(char2)]
	reflected = reflector(char3)
	char3 = alphabet[roter3.find(reflected)]
	char2 = alphabet[roter2.find(char3)]
	char1 = alphabet[roter1.find(char2)]

	return char1

def rotateRotor():
	global roter1, roter2, roter3
	roter1 = roter1[1:] + roter1[0]
	if state % 26 == 0:
		roter2 = roter2[1:] + roter2[0]
	if state % (26*26) == 0:
		roter2 = roter3[1:] + roter3[0]

text = input()
codedText = str()
state = 0

for c in text:
	state += 1
	codedText += codeCharacter(c)
	rotateRotor()

print(codedText)