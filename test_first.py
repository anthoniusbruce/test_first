import inspect

def are_equal(expected, actual, description = ""):
    result = inspect.stack()[1][3] + ": "  # the calling function name
    if (description != ""):
        result = result + description + ": "
    if (expected == actual):
        result = result + "success"
    else: 
        result = result + "FAIL\nexpected: {0}\nactual: {1}".format(expected, actual)

    print(result)
