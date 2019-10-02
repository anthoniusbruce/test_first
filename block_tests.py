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
    test_first.are_equal(True, block_result.hash is not None, "hash has a value")

def Block_hashing_pass_required_items_expect_repeatable_hash():
    #Assign
    index = 0
    timestamp = datetime.datetime(1999, 12, 31, 0, 0, 0)
    previous_hash = "101"
    kudo_rec = kudo.Kudo("andy@tr.com", "anthonius@tr.com", datetime.date(2010, 3, 5))
    expected_hash = "22cd5125dd3ee3d56ed6a315b8c6e121804f3dea0fcf06fb2c1cf1c54bdf1102"

    #Action
    actual_hash = block.Block.hashing(index, timestamp, previous_hash, kudo_rec)

    #Assert
    test_first.are_equal(expected_hash, actual_hash)

def Block_create_pass_negative_index_expect_IndexError_exception():
    #Assign
    index = -1
    timestamp = datetime.datetime(2011, 6, 29)
    previous_hash = "102"
    kudo_rec = kudo.Kudo("andy@tr.com", "anthonius@tr.com", datetime.date(1972, 4, 22))

    #Action and Assert
    try:
        block.Block(index, timestamp, previous_hash, kudo_rec)
        test_first.are_equal("exception", "no exception")
    except IndexError:
        test_first.are_equal("IndexError", "IndexError")
    except:
        test_first.are_equal("IndexError", "some other exception")

#Run tests
Block_create_pass_all_items_expect_object_with_all_items_and_a_hash()
Block_hashing_pass_required_items_expect_repeatable_hash()
Block_create_pass_negative_index_expect_IndexError_exception()