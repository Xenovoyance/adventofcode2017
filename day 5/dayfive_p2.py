my_list = []
x = 0
steps_taken = 0

with open('input_dayfive.txt') as f:
	for line in f:
		my_list.append(line.strip())

while (x < len(my_list)):
	loc = my_list[x]
	if (int(loc) >= 3):
		my_list[x] = int(loc) - 1
	else:
		my_list[x] = int(loc) + 1
	x = x + int(loc)
	steps_taken = steps_taken + 1

print "P2: " + str(steps_taken)
