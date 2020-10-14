run_env = "prod" ## test or prod

if run_env == "test":
    input = "test_input.txt"
else:
    input = "input_dayten.txt"

with open(input) as blockstream:
    for stream in blockstream:
        #
