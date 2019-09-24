import io
import contextlib
import inspect
import test_first

def capture_print(method, expected, actual, desc=""):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        if desc == "":
            method(expected, actual)
        else:
            method(expected, actual, desc)
    actual_out = output.getvalue().strip().rstrip()
    return actual_out

def evaluate_call(expected, actual):
    result = inspect.stack()[1][3] + ": "  # the calling function name
    if (expected == actual):
        result = result + "success"
    else: 
        result = result + "FAIL\nexpected: {0}\nactual: {1}".format(expected, actual)

    print(result)


def test_first_are_equal_pass_equal_integers_expect_success():
    #Assign
    expected = 1
    actual = 1
    expected_out = "capture_print: success"

    #Action
    actual_out = capture_print(test_first.are_equal, expected, actual)

    #Assert
    evaluate_call(expected_out, actual_out)

def test_first_are_equal_pass_unequal_integers_expect_FAIL():
    #Assign
    expected = 1
    actual = 2
    expected_out = "capture_print: FAIL\nexpected: {0}\nactual: {1}".format(expected, actual)
    
    #Action
    actual_out = capture_print(test_first.are_equal, expected, actual)

    #Assert
    evaluate_call(expected_out, actual_out)

def test_first_are_equal_pass_equal_strings_expect_success():
    #Assign
    expected = "a"
    actual = "a"
    expected_out = "capture_print: success"

    #Action
    actual_out = capture_print(test_first.are_equal, expected, actual)

    #Assert
    evaluate_call(expected_out, actual_out)

def test_first_are_equal_pass_unequal_strings_expect_FAIL():
    #Assign
    expected = "a"
    actual = "b"
    expected_out = "capture_print: FAIL\nexpected: {0}\nactual: {1}".format(expected, actual)
    
    #Action
    actual_out = capture_print(test_first.are_equal, expected, actual)

    #Assert
    evaluate_call(expected_out, actual_out)

def test_first_are_equal_pass_equal_integers_and_description_expect_success_with_description():
    #Assign
    expected = "a"
    actual = "a"
    description = "desc"
    expected_out = "capture_print: desc: success"
    
    #Action
    actual_out = capture_print(test_first.are_equal, expected, actual, description)

    #Assert
    evaluate_call(expected_out, actual_out)

def test_first_are_equal_pass_unequal_strings_and_description_expect_FAIL_with_description():
    #Assign
    expected = "a"
    actual = "b"
    description = "desc"
    expected_out = "capture_print: desc: FAIL\nexpected: {0}\nactual: {1}".format(expected, actual)
    
    #Action
    actual_out = capture_print(test_first.are_equal, expected, actual, description)

    #Assert
    evaluate_call(expected_out, actual_out)

#Run tests
test_first_are_equal_pass_equal_integers_expect_success()
test_first_are_equal_pass_unequal_integers_expect_FAIL()
test_first_are_equal_pass_equal_strings_expect_success()
test_first_are_equal_pass_unequal_strings_expect_FAIL()
test_first_are_equal_pass_equal_integers_and_description_expect_success_with_description()
test_first_are_equal_pass_unequal_strings_and_description_expect_FAIL_with_description()