import sys
result = []
itr = 0
balanced_nodes = []

run_env = "prod" ## test or prod

if run_env == "test":
    input = "test_input.txt"
else:
    input = "input_dayseven.txt"

def is_index_in_list(_index,_list):
    for x in range(0, len(_list)):
        if _list[x] == _index:
            return True
    return False

def print_childrens_weights(_id):
    "Find weights of childrens nodes"
    _weights = []
    print "----- " + get_name_from_id(_id) + "(" + str(result[_id]['weight']) + ") -------"
    for x in range(0, len(result)):
        if result[x]['parent'] == get_name_from_id(_id):
            _weights.append(result[x]['childrensWeight'])
    for x in range(0, len(_weights)):
        print _weights[x]
    print "------------"

def find_index(nodename):
    "Finding the index in list of the parent for the child sent in"
    for y in range(0, len(result)):
        if result[y]['name'] == nodename:
            return y
    return -1
    #print "!!! FATAL ERROR: find_index() got a bad node: " + str(nodename)
    #sys.exit(-1)

def find_p_index(nodename):
    "Find the index of a node name"
    for y in range(0, len(result)):
        if result[y]['name'] == nodename:
            # index found, let's find the parents
            return find_index(result[y]['parent'])
    return -1
    #print "!!! FATAL ERROR: find_p_index() got a bad node"
    #sys.exit(-1)

def get_name_from_id(_id):
    "Return name of id"
    return result[_id]['name']

def push_weight_to_parent(nodename):
    "Take a node as input and add the weight to it's parent"
    node_index = find_index(nodename)
    node_weight = result[node_index]['childrensWeight']
    node_p_index = find_p_index(nodename)
    #print "Pushing weight " + str(node_weight)  + " from " + nodename + "(" + str(node_index) + ") to " + get_name_from_id(node_p_index) + "(" + str(node_p_index) + ")"
    result[node_p_index]['childrensWeight'] += int(node_weight)
    return node_p_index

def is_tree_balanced(_id):
    "Check if all children are in balance"
    found_weights = []
    for x in range(0, len(result)):
        if result[x]['parent'] == get_name_from_id(_id):
            if is_index_in_list(result[x]['childrensWeight'], found_weights) is False:
                found_weights.append(result[x]['childrensWeight'])
    balanced_nodes.append(_id)
    if len(found_weights) == 1:
        return True
    return False

# first, let's map names and weights into the nodedict result
with open(input) as f: ## Test data
#with open('input_dayseven.txt') as f: ## Real data
    for line in f:
        nodedict = {}
        words = line.split()
        nodedict['name'] = words[0]
        nodedict['weight'] = int(words[1].strip('()'))
        nodedict['parent'] = ""
        nodedict['childrensWeight'] = int(words[1].strip('()'))
        if len(words) > 2:
            nodedict['haveChildren'] = True
        else:
            nodedict['haveChildren'] = False
        result.append(nodedict)
        itr += 1

# second time, let's map up parents
with open(input) as f: ## Test data
#with open('input_dayseven.txt') as f: ## Real data
    for line in f:
        words = line.split()
        if len(words) > 2:
            for x in range(3, len(words)):
                p_index = find_index(words[x].strip(','))
                result[p_index]['parent'] = words[0]

# Third time, build composit weights
next_nodes = []
for x in range(0, len(result)):
    if result[x]['haveChildren'] == False:
        _p_index = push_weight_to_parent(result[x]['name'])
        if is_index_in_list(_p_index, next_nodes) is False:
            next_nodes.append(_p_index)
"""
for z in range(0, len(result)):
    print "(" + str(z) + ")" + str(result[z])
"""

no_not_balanced = 1

while len(next_nodes) > 0:
    if is_tree_balanced(next_nodes[0]):
        result[next_nodes[0]]['isBalanced'] = True
        #print "Balanced below"
        #print_childrens_weights(next_nodes[0])
    else:
        result[next_nodes[0]]['isBalanced'] = False
        print str(no_not_balanced) + " | NOT Balanced below"
        no_not_balanced += 1
        print_childrens_weights(next_nodes[0])
    _name = get_name_from_id(next_nodes[0])
    _p_index = push_weight_to_parent(_name)
    if (is_index_in_list(_p_index, next_nodes) == False) and (_p_index != -1):
        next_nodes.append(_p_index)
    next_nodes.pop(0)

"""
Suggested solution
1. Find starting next_nodes == leafs                            find_leafs, build next_nodes
2. Send all weights from startnodes to parents                  iterate next_nodes, push_weight_to_parent
3. All parents that get weights are added to next_nodes list    next_nodes = return from push_weight_to_parent
"""

for x in range(0, len(result)):
    if result[x]['parent'] == '':
        top_node = result[x]['name']
        print "Top node is: %s" % top_node
        if run_env == "test":
            assert result[x]['name'] == 'tknk' ## Test data
        else:
            assert result[x]['name'] == 'airlri' ## Real data

# Ok, so to find the difference in weight then
# start by finding all nodes that hade the top node as parents
# compare their weights and find the difference between them all
#print second_layer_weight

for z in range(0, len(result)):
    if is_index_in_list(z, balanced_nodes):
        print result[z]
