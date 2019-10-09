import kudo
import datetime
import test_first
import kudo_jsonencoder

def KudoJSONEncoder_default_pass_Kudo_expect_well_formed_JSON_Kudo():
    #Assign
    kudo_rec = kudo.Kudo("recip1", "nom1", datetime.date(1972, 4, 22))
    expected_json = '{"recipient": "recip1", "nominator": "nom1", "date": "1972-04-22"}'
    encoder = kudo_jsonencoder.KudoJSONEncoder()

    #Action
    actual_json = encoder.encode(kudo_rec)

    #Assert
    test_first.are_equal(expected_json, actual_json)

#Run tests
KudoJSONEncoder_default_pass_Kudo_expect_well_formed_JSON_Kudo()