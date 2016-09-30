def caserestore(digit, word):
	if digit == 0:
		word = word.lower()
	if digit == 1:
		word = word.title()
	if digit == 2:
		word = word.upper()
	return word

print caserestore(0, 'aksjdh')
print caserestore(1, 'akjsdh')
print caserestore(2, 'asdjkjah')

def checkcase(word):
	if word.islower():
		return 0
	if word.istitle():
		return 1
	if word.isupper():
		return 2
	else:
		pass

print checkcase('wqiuhq')
print checkcase('Wqiuhq')
print checkcase('DKJUIH')
print checkcase('_Wqiuh__')


def peek(string, words_of_interest):

	for word in words_of_interest:
		if word in string.lower() \
			and len(string) / len(word) < 2:
			return word

print peek('HELLOsss', ['hel'])