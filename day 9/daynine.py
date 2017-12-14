run_env = "test" ## test or prod

if run_env == "test":
    input = "test_input.txt"
else:
    input = "input_daynine.txt"

block_level = 0
row_score = 0
skip_next = False

def check_block(_stream, _id):
    "Block finder"
    global block_level
    global row_score
    global skip_next
    _char_index = _id

    if _char_index >= len(_stream) - 1:
        return _char_index
    if skip_next is False:
        if _stream[_char_index] == '!':
            skip_next = True
        elif _stream[_char_index] == '{':
            block_level += 1
            check_block(_stream, _char_index + 1)
        elif _stream[_char_index] == '}':
            row_score = row_score + block_level
            block_level -= 1
            return _char_index + 1
    else:
        skip_next = False

with open(input) as blockstream:
    for stream in blockstream:
        stream.rstrip(' ,\n\r')
        char_index = 0
        while True:
            if char_index >= len(stream) - 1:
                break
            if skip_next is False:
                char_index = check_block(stream, char_index)
            else:
                skip_next = False
            char_index += 1
        print "Row score: %d" % row_score

# Known issues: !! will not work
