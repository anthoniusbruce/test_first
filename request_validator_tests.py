import test_first
import request_validator

def RequestValidator_validate_post_pass_recipient_nominator_date_expect_True():
    #Assign
    json = {"recipient": "recip", "nominator":"nom", "date":"2001-01-01"}

    #Action
    result = request_validator.RequestValidator.validate_post(json)

    #Assert
    test_first.are_equal(True, result[0])

def RequestValidator_validate_post_pass_nominator_date_expect_False_Missing_Recipient():
    #Assign
    json = {"nominator":"nom", "date":"2001-01-01"}
    expected_error = "missing recipient"

    #Action
    result = request_validator.RequestValidator.validate_post(json)

    #Assert
    test_first.are_equal(False, result[0])
    test_first.are_equal(expected_error, result[1])

def RequestValidator_validate_post_pass_recipient_date_expect_False_Missing_Nominator():
    #Assign
    json = {"recipient":"recip", "date":"2001-01-01"}
    expected_error = "missing nominator"

    #Action
    result = request_validator.RequestValidator.validate_post(json)

    #Assert
    test_first.are_equal(False, result[0])
    test_first.are_equal(expected_error, result[1])

def RequestValidator_validate_post_pass_recipient_nominator_expect_False_Missing_Date():
    #Assign
    json = {"recipient":"recip", "nominator":"nom"}
    expected_error = "missing date"

    #Action
    result = request_validator.RequestValidator.validate_post(json)

    #Assert
    test_first.are_equal(False, result[0])
    test_first.are_equal(expected_error, result[1])

def RequestValidator_validate_post_pass_recipient_expect_False_Missing_Nominator_Date():
    #Assign
    json = {"recipient":"recip"}
    expected_error = "missing nominator, date"

    #Action
    result = request_validator.RequestValidator.validate_post(json)

    #Assert
    test_first.are_equal(False, result[0])
    test_first.are_equal(expected_error, result[1])

def RequestValidator_validate_post_pass_None_expect_False_Missing_Kudo():
    #Assign
    json = None
    expected_error = "missing kudo"

    #Action
    result = request_validator.RequestValidator.validate_post(json)

    #Assert
    test_first.are_equal(False, result[0])
    test_first.are_equal(expected_error, result[1])

def RequestValidator_validate_post_pass_matching_recipient_and_nominator_expect_False_recipient_cannot_match_nominator():
    #Assign
    json = {"recipient": "recip", "nominator":"recip", "date":"2001-01-01"}

    expected_error = "recipient cannot not match nominator"

    #Action
    result = request_validator.RequestValidator.validate_post(json)

    #Assert
    test_first.are_equal(False, result[0])
    test_first.are_equal(expected_error, result[1])

#Run tests
RequestValidator_validate_post_pass_recipient_nominator_date_expect_True()
RequestValidator_validate_post_pass_nominator_date_expect_False_Missing_Recipient()
RequestValidator_validate_post_pass_recipient_date_expect_False_Missing_Nominator()
RequestValidator_validate_post_pass_recipient_nominator_expect_False_Missing_Date()
RequestValidator_validate_post_pass_recipient_expect_False_Missing_Nominator_Date()
RequestValidator_validate_post_pass_None_expect_False_Missing_Kudo()
RequestValidator_validate_post_pass_matching_recipient_and_nominator_expect_False_recipient_cannot_match_nominator()
