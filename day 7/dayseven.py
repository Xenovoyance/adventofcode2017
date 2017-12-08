#!/usr/bin/python
result = []
itr = 0

def find_p_index(nodename):
    "Finding the index in list of the parent for the child sent in"
    for y in range(0, len(result)):
        if result[y]['name'] == nodename:
            return y
    return -1

with open('test_input.txt') as f:
#with open('input_dayseven.txt') as f:
    # first, let's map names and weights into the nodedict result
    for line in f:
        nodedict = {}
        words = line.split()
        nodedict['name'] = words[0]
        nodedict['weight'] = words[1].strip('()')
        nodedict['parent'] = ""
        nodedict['childrensWeight'] = 0
        if len(words) > 2:
            nodedict['haveChildren'] = True
        else:
            nodedict['haveChildren'] = False
        result.append(nodedict)
        itr += 1

with open('test_input.txt') as f:
#with open('input_dayseven.txt') as f:
    # second time, let's map up parents
    for line in f:
        words = line.split()
        if len(words) > 2:
            for x in range(3, len(words)):
                p_index = find_p_index(words[x].strip(','))
                result[p_index]['parent'] = words[0]
                result[p_index]['childrensWeight'] += int(words[1].strip('()'))

result.sort()

print "Top node is: %s" % result[0]['name']

# Assert to see that it is still working with the correct input
#assert result[0]['name'] == 'airlri'

for z in range(0, len(result)):
    print result[z]
"""    if result[z]['parent']:
        if result[z]['parent'] == "airlri":
            print result[z]"""
