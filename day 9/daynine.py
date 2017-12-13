run_env = "test" ## test or prod

if run_env == "test":
    input = "test_input.txt"
else:
    input = "input_dayeight.txt"

block_level = 0
row_score = 0

def found_block(_stream, _id):
    "Block finder"
    global block_level
    global row_score
    _skip_next = False
    _char_index = _id
    block_level += 1
    while True:
        print "Char index: %d" % _char_index
        if _skip_next is False:
            if _stream[_char_index] == '!':
                _skip_next = True
            elif _stream[_char_index] == '{':
                found_block(_stream, _char_index + 1)
            elif _stream[_char_index] == '}':
                row_score += block_level
                print "Level: %s" % block_level
                block_level -= 1
                return _char_index
        else:
            _skip_next = False
        _char_index += 1
        if _char_index >= len(_stream):
            return -1

with open(input) as blockstream:
    for stream in blockstream:
        skip_next = False
        char_index = 0
        while True:
            print "Char index: %d" % char_index
            if skip_next is False:
                if stream[char_index] == '!':
                    skip_next = True
                elif stream[char_index] == '{':
                    char_index = found_block(stream, char_index + 1)
            else:
                skip_next = False
            char_index += 1
            if char_index >= len(stream):
                break
        print "Row score: %d" % row_score


"""
Known issues: !! will not work
"""
