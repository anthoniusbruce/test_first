import inspect

def are_equal(expected, actual, description = ""):
    result = inspect.stack()[1][3] + ": "  # the calling function name
    if (description != ""):
        result = result + description + ": "
    if (expected == actual):
        result = result + "\033[92msuccess\033[00m"
    else: 
        result = result + "\033[91mFAIL\033[00m\n\texpected: {0}\n\tactual: {1}".format(expected, actual)

    print(result)
