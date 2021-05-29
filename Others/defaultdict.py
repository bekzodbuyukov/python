from collections import defaultdict


# return default value for not existing keys
def return_default_value():
    return "Value doesn't exist"


# create dict using defaultdict
test_dict = defaultdict(return_default_value)

# add data to dict in key:value syntax
test_dict["a"] = "Letter: a"
test_dict["b"] = "Letter: b"

if __name__ == "__main__":
    # print dict elements by keys
    print(test_dict["a"])
    print(test_dict["b"])

    # try to print value for not existing key
    print(test_dict["c"])
