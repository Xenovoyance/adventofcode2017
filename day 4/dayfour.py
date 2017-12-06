non_duplicates = 0
non_anagram = 0

def is_anagram(w1, w2):
    w1, w2 = list(w1.upper()), list(w2.upper())
    w2.sort()
    w1.sort()
    return w1 == w2

with open('input_dayfour.txt') as f:
	for line in f:
		words = line.split()
		words.sort()
		
		dups = 0
		anagrams = 0
		last_word = ""

		for x in range(0,len(words)):
			for y in range(0,len(words)):
				if (x!=y) and (is_anagram(words[x], words[y])):
					anagrams = anagrams + 1
					break

			if (last_word == words[x]):
				dups = dups + 1

			last_word = words[x]

		if (dups == 0):
			non_duplicates = non_duplicates + 1
		if (anagrams == 0):
			non_anagram = non_anagram + 1

print "P1: " + str(non_duplicates)
print "P2: " + str(non_anagram)

# P2: 350 too high
# P2 Not 105
# P2 Not 293