run_env = "test" ## test or prod

if run_env == "prod":
    input = "test_input.txt"
else:
    input = "input_daynine.txt"

block_level = 0
row_score = 0
skip_next = False
is_garbage = False

with open(input) as blockstream:
    for stream in blockstream:
        stream.rstrip(' ,\n\r')
        char_index = 0
        block_level = 0
        row_score = 0
        skip_next = False
        is_garbage = False
        while True:
            if char_index >= len(stream) - 1:
                break
            if skip_next is True:
                skip_next = False
            else:
                if stream[char_index] == "<":
                    is_garbage = True
                if stream[char_index] == "!":
                    skip_next = True
                elif is_garbage is False:
                    if stream[char_index] == "{":
                        block_level += 1
                    if stream[char_index] == "}":
                        row_score += block_level
                        block_level -= 1
                else:
                    if stream[char_index] == ">":
                        is_garbage = False
            char_index += 1
        print "Row score: %d" % row_score
        if row_score != 13154:
            print "Something broke the code. Go back."

# Known issues: !! will not work
