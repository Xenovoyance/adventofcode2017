# initialize the p1_matrix
p1_matrix = [[0 for i in xrange(1000)] for i in xrange(1000)]

p1_matrix[0][0] = 1
p1_matrix[1][0] = 2
p1_matrix[1][1] = 3

last_x = 1
last_y = 1

# define progression path logic selectors
p1_rep_counter = 2
p1_rep_counter_iterator = 2
p1_rep_switch = False
p1_direction = "left"

x = 4

# build the P1 spiral and break when we find our number
while (x < 300000):
	if (p1_rep_counter_iterator > 0):
		if (p1_direction == "left"):
			last_x = last_x -1
			p1_matrix[last_x][last_y] = x
			x = x + 1
			p1_rep_counter_iterator = p1_rep_counter_iterator -1
			if (p1_rep_counter_iterator == 0):
				p1_direction = "down"
		elif (p1_direction == "down"):
			last_y = last_y -1
			p1_matrix[last_x][last_y] = x
			x = x + 1
			p1_rep_counter_iterator = p1_rep_counter_iterator -1
			if (p1_rep_counter_iterator == 0):
				p1_direction = "right"
		elif (p1_direction == "right"):
			last_x = last_x +1
			p1_matrix[last_x][last_y] = x
			x = x + 1
			p1_rep_counter_iterator = p1_rep_counter_iterator -1
			if (p1_rep_counter_iterator == 0):
				p1_direction = "up"
		elif (p1_direction == "up"):
			last_y = last_y + 1
			p1_matrix[last_x][last_y] = x
			x = x + 1
			p1_rep_counter_iterator = p1_rep_counter_iterator -1
			if (p1_rep_counter_iterator == 0):
				p1_direction = "left"
	else:
		if (p1_rep_switch):
			p1_rep_counter = p1_rep_counter +1
			p1_rep_switch = False
		else:
			p1_rep_switch = True
		p1_rep_counter_iterator = p1_rep_counter
	if (x > 277678):
		break

if ((abs(last_x)+abs(last_y)) != 475):
	print "!!! [ERROR] in P1 sprial! Should be 475 but was " + str(abs(last_x)+abs(last_y))

# print the distance from number to center
print "P1: " + str(abs(last_x)+abs(last_y))