# first hash is -5530013683313969476

banks = [5,1,10,0,1,7,13,14,3,12,8,10,7,12,0,6]
hashes = []
iterations = 0

def is_checksum_unique(checksum):
    "Checking an checksum against known hashes"
    try:
        found_index = hashes.index(checksum)
    except ValueError:
        found_index = -1
    if (found_index == -1):
        return True
    else:
        return False

while (True):
    max_value = max(banks)
    start_index = int(banks.index(max(banks)))
    max_value_blocks = int(banks[int(banks.index(max(banks)))])

    banks[start_index] = 0

    # Check if we are at the end of the list of banks
    if (start_index == len(banks) - 1):
        start_index = 0
    else:
        start_index = start_index + 1

    while (max_value_blocks > 0):
        # As long as we have blocks left to distribute, loop
        # Move to next block and increase by one
        banks[start_index] = banks[start_index] + 1

        # Check if we are at the end of the list of banks
        if ((start_index + 1) > len(banks) - 1):
            start_index = 0
        else:
            start_index = start_index + 1

        # reduce the amount of blocks by one
        max_value_blocks =  max_value_blocks - 1

    iterations = iterations + 1

    if (is_checksum_unique(hash(tuple(banks)))):
        hashes.append(hash(tuple(banks)))
    else:
        print "No longer unique after " + str(iterations) + " iterations."
        print "The matching hash was found at location " + str(hashes.index(hash(tuple(banks)))) + ". That was " + str(iterations - hashes.index(hash(tuple(banks))) - 1) + " steps."
        break

    # 14037 too high, 5041 too low
    if (iterations > 15000):
        break
