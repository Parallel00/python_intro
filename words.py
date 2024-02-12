def print_upper_words(wrd):
	for words in wrd:
		print(words.upper())

def print_upper_words_second(wrd):
	for words in wrd:
		if words.startswith("e") or words.startswith("E"):
			print(words.upper())

def print_upper_words_third(wrd, must_start_with):
	for words in wrd:
		for ltr in must_start_with:
			if wrd.startswith(ltr):
				print (words.upper())
				break