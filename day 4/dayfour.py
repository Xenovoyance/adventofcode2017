non_duplicates = 0

with open('input_dayfour.txt') as f:
	for line in f:
		words = line.split()
		words.sort()

		dups = 0
		last_word = ""

		for x in range(0,len(words)):
			if (last_word == words[x]):
				dups = dups + 1
			last_word = words[x]

		if (dups == 0):
			non_duplicates = non_duplicates + 1

print non_duplicates