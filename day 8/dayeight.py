run_env = "prod" ## test or prod
register_values = []
register_names = []
largest = 0

if run_env == "test":
    input = "test_input.txt"
else:
    input = "input_dayeight.txt"

def if_not_known_add(_string):
    "See if register exist, else add it with value 0"
    try:
        register_names.index(_string)
    except ValueError:
        register_values.append(0)
        register_names.append(_string)

def increase_value(_amount, _register):
    "Increase values"
    global largest
    reg_id = register_names.index(_register)
    register_values[reg_id] += int(_amount)
    if register_values[reg_id] > largest:
        largest = register_values[reg_id]

def decrese_value(_amount, _register):
    "Decrease value"
    global largest
    reg_id = register_names.index(_register)
    register_values[reg_id] -= int(_amount)
    if register_values[reg_id] > largest:
        largest = register_values[reg_id]

with open(input) as f:
    for instruction in f:
        words = instruction.split()
        print register_values
        print words[1]
        if_not_known_add(words[0])
        if_not_known_add(words[4])
        if words[5] == ">":
            if register_values[register_names.index(words[4])] > int(words[6]):
                if words[1] == "inc":
                    increase_value(words[2],words[0])
                else:
                    decrese_value(words[2],words[0])
        elif words[5] == "<":
            if register_values[register_names.index(words[4])] < int(words[6]):
                if words[1] == "inc":
                    increase_value(words[2],words[0])
                else:
                    decrese_value(words[2],words[0])
        elif words[5] == "==":
            if register_values[register_names.index(words[4])] == int(words[6]):
                if words[1] == "inc":
                    increase_value(words[2],words[0])
                else:
                    decrese_value(words[2],words[0])
        elif words[5] == "!=":
            if register_values[register_names.index(words[4])] != int(words[6]):
                if words[1] == "inc":
                    increase_value(words[2],words[0])
                else:
                    decrese_value(words[2],words[0])
        elif words[5] == ">=":
            if register_values[register_names.index(words[4])] >= int(words[6]):
                if words[1] == "inc":
                    increase_value(words[2],words[0])
                else:
                    decrese_value(words[2],words[0])
        elif words[5] == "<=":
            if register_values[register_names.index(words[4])] <= int(words[6]):
                if words[1] == "inc":
                    increase_value(words[2],words[0])
                else:
                    decrese_value(words[2],words[0])


register_values.sort()

print largest
