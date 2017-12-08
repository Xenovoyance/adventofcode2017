#!/usr/bin/python
result = []
itr = 0

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

    # second time, let's map up parents
    for line in f:
        words = line.split()
        print len(words)
        """
        if len(words) > 2:
            for x in range(3,len(words)):
                # find parent for the node we're at and update the dict
                print words[x]
                """

#print result
