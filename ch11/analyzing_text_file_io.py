def count_words(filename):
	"""Count the number of words in a file, approximately"""

	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist.."
		print(msg)

	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words..")


filename = 'Dhammapada.txt'
count_words(filename)