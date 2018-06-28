def count_words(filename):
	"""Count the number of words in a file, approximately"""

	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist.."
		# could pass here if we didnt want user to know anyting 
		print(msg)

	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words..")


filenames = ['Dhammapada.txt', 'siddartha.txt']
for filename in filenames:
	count_words(filename)