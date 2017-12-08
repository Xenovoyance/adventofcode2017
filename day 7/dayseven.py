#!/usr/bin/python
result = []
itr = 0

def find_parent_index(nodename):
    "Finding the index in list of the parent for the child sent in"
    for y in range(0,len(result)):
        if result[y]['name'] == nodename:
            return y
    return -1

with open('input_dayseven.txt') as f:
    # first, let's map names and weights into the dict result
    for line in f:
        dict = {}
        words = line.split()
        dict['name'] = words[0]
        dict['weight'] = words[1]
        if len(words) > 2:
            dict['haveChildren'] = True
        else:
            dict['haveChildren'] = False
        result.append(dict)
        itr = itr + 1

with open('input_dayseven.txt') as f:
    # second time, let's map up parents
    for line in f:
        words = line.split()
        if len(words) > 2:
            for x in range(3,len(words)):
                result[find_parent_index(words[x].strip(','))]['parent'] = words[0]

result.sort()
print "Top node is: " + result[0]['name']

# Assert to see that it is still working with the correct input
assert result[0]['name'] == 'airlri'
