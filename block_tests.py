import datetime
import kudo
import test_first
import block

def Block_create_pass_all_items_expect_object_with_all_items_and_a_hash():
    #Assign
    expected_index = 1
    expected_timestamp = datetime.datetime(1972, 4, 22, 0, 0, 0)
    expected_previous_hash = 100
    expected_kudo = kudo.Kudo("andy@tr.com", "anthonius@tr.com", datetime.date(1972, 4, 22))

    #Action
    block_result = block.Block(expected_index, expected_timestamp, expected_previous_hash, expected_kudo)

    #Assert
    test_first.are_equal(expected_index, block_result.index, "index")
    test_first.are_equal(expected_timestamp, block_result.timestamp, "timestamp")
    test_first.are_equal(expected_previous_hash, block_result.previous_hash, "previous hash")
    test_first.are_equal(expected_kudo.recipient, block_result.kudo.recipient, "kudo.recipient")
    test_first.are_equal(expected_kudo.nominator, block_result.kudo.nominator, "kudo.nominator")
    test_first.are_equal(expected_kudo.date, block_result.kudo.date, "kudo.date")
    
#Run tests
Block_create_pass_all_items_expect_object_with_all_items_and_a_hash()