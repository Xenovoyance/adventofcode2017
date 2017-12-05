# initialize the matrix
matrix = [[0 for i in xrange(1000)] for i in xrange(1000)]

matrix[0][0] = 1
matrix[1][0] = 2
matrix[1][1] = 3

last_x = 1
last_y = 1

# define progression path logic selectors
rep_counter = 2
rep_counter_iterator = 2
rep_switch = False
direction = "left"

x = 4

# build the spiral and break when we find our number
while (x < 300000):
	if (rep_counter_iterator > 0):
		if (direction == "left"):
			last_x = last_x -1
			matrix[last_x][last_y] = x
			if (x == 277678):
				break
			x = x + 1
			rep_counter_iterator = rep_counter_iterator -1
			if (rep_counter_iterator == 0):
				direction = "down"
		elif (direction == "down"):
			last_y = last_y -1
			matrix[last_x][last_y] = x
			if (x == 277678):
				break
			x = x + 1
			rep_counter_iterator = rep_counter_iterator -1
			if (rep_counter_iterator == 0):
				direction = "right"
		elif (direction == "right"):
			last_x = last_x +1
			matrix[last_x][last_y] = x
			if (x == 277678):
				break
			x = x + 1
			rep_counter_iterator = rep_counter_iterator -1
			if (rep_counter_iterator == 0):
				direction = "up"
		elif (direction == "up"):
			last_y = last_y +1
			matrix[last_x][last_y] = x
			if (x == 277678):
				break
			x = x + 1
			rep_counter_iterator = rep_counter_iterator -1
			if (rep_counter_iterator == 0):
				direction = "left"
	else:
		if (rep_switch):
			rep_counter = rep_counter +1
			rep_switch = False
		else:
			rep_switch = True
		rep_counter_iterator = rep_counter

# print the distance from number to center
print abs(last_x)+abs(last_y)