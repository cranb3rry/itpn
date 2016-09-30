
# These and *_game_content should match
difficulties_list = ["easy", "normal", "hard"]

easy_game_content = """A common first thing to do in a language is display "Hello, world!". In Python this is particularly easy; all you have to do is type in: print "Hello, world!"

Of course, that isn't a very useful thing to do.
However, it is an example 
of how to output to the user using the print command, and produces 
a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that 
can be done even more easily with an HTML file in a browser, 
but it's a step in learning python syntax, and that's really its purpose."""

normal_game_content = """A procedure is created with the def keyword. 
You specify the inputs a procedure takes by
adding arguments separated by commas between the parentheses. 
Procedures by default return None if you don't specify the value to return. 
Arguments can be standard data types such as string, number, dictionary,
tuple, and list or can be more complicated such as objects and lambda functions."""

hard_game_content = """When you create a class, certain methods are automatically 
generated for you if you don't make them manually. These contain multiple 
underscores before and after the word defining them. When you write a class,
you almost always include at least the __init__ method, defining variables for
when instances of class get made. Additionally, you generally want to create a
__repr__ method, which will allow a string representation of the method to be
viewed by other developers.
You can also create binary operators, like __add__ and __sub__, which allow +
and - to be used by instances of the class.
Similalry, __lt__, __gt__, and __eq__ allow instances of the class to be
compared with <, >, and ==."""

# All lowercase
words_of_interest = ("class", "method", "print", "html", "python", "hello", "def",
 "procedure", "none", "dictionary", "argument",
 "__init__", "instance", "__init__", "__repr__", "__add__", "__sub__",
  "__lt__", "__gt__", "__eq__")

# matches 'def' in 'def' or 'Defs.' but not in "definition" 
# because it's too long
# returns one of words_of_interest if match
def peek(string, words_of_interest):

	for word in words_of_interest:
		if word in string.lower() \
			and len(string) / len(word) < 2:
			return word

	return

# case of replaced answer strings are kept in answers dict
# so it would be possible to restore 'HTML' or 'html' like it was in
# original text

def checkcase(word):

	if word.istitle():
		return 1
	elif word.isupper():
		return 2
	else:
		return 0

# reverse of checkcase()
def caserestore(word, digit):

	if digit == 0:
		word = word.lower()
	elif digit == 1:
		word = word.title()
	elif digit == 2:
		word = word.upper()
	else:
		pass
	return word

# Separates game content from words_of_interest,
# Creates answers dict {answer: [index, case1, case2, ...]}
# for each word_of_interest found,
# places '__index__' cap in text instead

def separate(game_content, words):

	separated_from_words, answers, splitted_content, index = [], {}, game_content.split(), 1
	
	for string in splitted_content:

		replacement = peek(string, words_of_interest)
		
		if replacement != None:	

			if replacement not in answers:
				answers[replacement] = [index]
				index += 1

			answers[replacement].append(checkcase(string))

			cap = string.lower().replace(replacement, '__' \
				 + str(answers[replacement][0]) + '__')

			separated_from_words.append(cap)
			
		else:

			separated_from_words.append(string)

	separated_from_words = ' '.join(separated_from_words)
	
	return separated_from_words, answers

# reverse of separate()
# joins answers{} with separated_content
# from {answer:(index1, ..)} to {answer:(index2, ..)} etc... 
# each step requies user_input
# if right input continues to right_answer()
# ends with empty answers{}

def fill_in(separated, answers):

	print separated + "\n"

	if answers:

		answer = min(answers, key=answers.get)
		user_input = raw_input('> Try #' + str(answers[answer][0]) + ' ')

		if user_input.lower() == answer:

			print "\nRight!\n"

			separated, answers = right_answer(separated, answers, answer)

			fill_in(separated, answers)

		else:

			wrong_asnwer(separated, answers)

	else:

		print "You won!\n"
		start(False)

	return

# continuation of fill_in()
# asks to try once again

def wrong_asnwer(separated, answers):
		
	print "\nWrong.\n"

	user_input = raw_input('> Try again? ')

	if user_input.lower() in ('yes', 'y'):
		fill_in(separated, answers)
	else:
		print "\nGame over...\n"
		start(False)		
		
# launched for each {answer} by fill_in()
# for each string in text replaces caps with
# original word matched in ..{answer:(... ,case1, case2, ... )}

def right_answer(separated, answers, answer):

	splitted = separated.split(' ')
	renewed_content = []

	key = answers[answer][0]
	cap = '__'  + str(key) + '__'

	for word in splitted:

		if  cap in word:

			word = word.replace(cap, \
				caserestore(answer, answers[answer].pop(1)))

			renewed_content.append(word)
			
		else:

			renewed_content.append(word)

	del answers[answer]

	return ' '.join(renewed_content), answers

# Matches content with difficulty
# launches main functions
# separate() and fill_in()
def engine(difficulty):

	game_content = eval(difficulty + "_game_content")
		
	replaced, answers = \
		separate(game_content, words_of_interest)
	
	fill_in(replaced, answers)

# game menu, feeds difficulty to engine()
def start(intro):

	difficulty = ""

	if intro == True:
		print "Welcome to Fill In The Blanks!"

	print "Choose difficulty from " + \
	"/".join([x for x in difficulties_list]) + " or exit."
	
	start_input = raw_input("> ")
	
	if start_input == "exit":
		exit()
	elif start_input in difficulties_list:
		difficulty = start_input
		print "\nDifficulty set to " + difficulty + "." + \
				"\nFill in the blanks.\n"
		engine(difficulty)
	else:
		print "..."
		start(False)

start(True)