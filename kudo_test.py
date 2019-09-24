import datetime
import test_first
import kudo

def Kudo_create_pass_all_items_expect_Kudo_with_all_items():
    #Assign
    expected_recipient = "andy@tr.com"
    expected_nominator = "anthonius@tr.com"
    expected_date = datetime.date(1972, 4, 22)

    #Action
    actual = kudo.Kudo(expected_recipient, expected_nominator, expected_date)

    #Assert
    test_first.are_equal(expected_recipient, actual.recipient, "recipient")
    test_first.are_equal(expected_nominator, actual.nominator, "nominator")
    test_first.are_equal(expected_date, actual.date, "date")

#Run tests
Kudo_create_pass_all_items_expect_Kudo_with_all_items()