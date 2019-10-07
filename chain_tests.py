import test_first
import chain
import datetime
import kudo

def Chain_create_expect_list_with_the_genesis_block():
    #Action
    theChain = chain.Chain()

    #Assert
    test_first.are_equal(1, len(theChain.blocks), "One block is create")

def Chain_get_genesis_block_expect_a_block_with_genesis_info():
    #Assign
    expected_index = 0
    expected_timestamp = datetime.datetime(1972, 4, 22, 0, 0, 0)
    expected_previous_hash = "previous_hash"
    expected_recipient = ""
    expected_nominator = ""
    expected_date = datetime.date(1994, 6, 13)
    expected_hash = "81dd14b60acc3e90ddf5a08f5704eb890616dabc922659626026db6f81546692"

    #Action
    block_result = chain.Chain.get_genesis_block(expected_timestamp, expected_previous_hash, expected_date)

    #Assert
    test_first.are_equal(expected_index, block_result.index, "index")
    test_first.are_equal(expected_timestamp, block_result.timestamp, "timestamp")
    test_first.are_equal(expected_previous_hash, block_result.previous_hash, "previous_hash")
    test_first.are_equal(expected_recipient, block_result.kudo.recipient, "recepient")
    test_first.are_equal(expected_nominator, block_result.kudo.nominator, "nominator")
    test_first.are_equal(expected_date, block_result.kudo.date, "date")
    test_first.are_equal(expected_hash, block_result.hash, "hash")

def Chain_add_block_expect_index_of_well_formed_block():
    #Assign
    theChain = chain.Chain()
    expected_index = 1
    expected_recipient = "andy@tr.com"
    expected_nominator = "anthonius@tr.com"
    expected_date = datetime.date(1972, 4, 22)

    #Action
    actual_index = theChain.add_block(expected_recipient, expected_nominator, expected_date)

    #Assert
    test_first.are_equal(expected_index, actual_index, "actual index")
    test_first.are_equal(expected_index, theChain.blocks[actual_index].index, "block index")
    test_first.are_equal(expected_recipient, theChain.blocks[actual_index].kudo.recipient, "recipient")
    test_first.are_equal(expected_nominator, theChain.blocks[actual_index].kudo.nominator, "nominator")
    test_first.are_equal(expected_date, theChain.blocks[actual_index].kudo.date, "date")
    test_first.are_equal(theChain.blocks[0].hash, theChain.blocks[actual_index].previous_hash, "previous hash matches")

#Run tests
Chain_create_expect_list_with_the_genesis_block()
Chain_get_genesis_block_expect_a_block_with_genesis_info()
Chain_add_block_expect_index_of_well_formed_block()