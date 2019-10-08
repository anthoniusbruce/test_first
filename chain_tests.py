import test_first
import chain
import datetime
import kudo

def Chain_create_expect_list_with_the_genesis_block():
    #Action
    theChain = chain.Chain()

    #Assert
    test_first.are_equal(1, len(theChain.blocks), "One block is created")

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

def Chain_verify_add_3_blocks_expect_True():
    #Assign
    theChain = chain.Chain()
    today = datetime.date.today()
    theChain.add_block("recip1", "nom1", today)
    theChain.add_block("recip2", "nom2", today)
    theChain.add_block("recip3", "nom3", today)

    #Action
    result = theChain.verify()

    #Assert
    test_first.are_equal(True, result)

def Chain_verify_remove_block_expect_False():
    #Assign
    theChain = chain.Chain()
    today = datetime.date.today()
    theChain.add_block("recip1", "nom1", today)
    theChain.add_block("recip2", "nom2", today)
    theChain.add_block("recip3", "nom3", today)
    theChain.blocks.remove(theChain.blocks[2])

    #Action
    result = theChain.verify()

    #Assert
    test_first.are_equal(False, result)

def Chain_verify_reorder_block_expect_False():
    #Assign
    theChain = chain.Chain()
    today = datetime.date.today()
    theChain.add_block("recip1", "nom1", today)
    theChain.add_block("recip2", "nom2", today)
    theChain.add_block("recip3", "nom3", today)
    hold_block = theChain.blocks[2]
    theChain.blocks.remove(theChain.blocks[2])
    theChain.blocks.append(hold_block)

    #Action
    result = theChain.verify()

    #Assert
    test_first.are_equal(False, result)

def Chain_verify_replace_block_expect_False():
    #Assign
    theChain = chain.Chain()
    today = datetime.date.today()
    theChain.add_block("recip1", "nom1", today)
    theChain.add_block("recip2", "nom2", today)
    theChain.add_block("recip3", "nom3", today)
    theChain.blocks.remove(theChain.blocks[2])
    alt_chain = chain.Chain()
    alt_chain.add_block("recip1", "nom1", today)
    alt_chain.add_block("recip2", "nom2", today)
    theChain.blocks.insert(2, alt_chain.blocks[2])

    #Action
    result = theChain.verify()

    #Assert
    test_first.are_equal(False, result)

def Chain_verify_change_block_expect_False():
    #Assign
    theChain = chain.Chain()
    today = datetime.date.today()
    theChain.add_block("recip1", "nom1", today)
    theChain.add_block("recip2", "nom2", today)
    theChain.add_block("recip3", "nom3", today)
    theChain.blocks[2].timestamp = datetime.datetime.utcnow()

    #Action
    result = theChain.verify()

    #Assert
    test_first.are_equal(False, result)

def Chain_verify_no_blocks_added_expect_True():
    #Assign
    theChain = chain.Chain()

    #Action
    result = theChain.verify()

    #Assert
    test_first.are_equal(True, result)

#Run tests
Chain_create_expect_list_with_the_genesis_block()
Chain_get_genesis_block_expect_a_block_with_genesis_info()
Chain_add_block_expect_index_of_well_formed_block()
Chain_verify_add_3_blocks_expect_True()
Chain_verify_remove_block_expect_False()
Chain_verify_reorder_block_expect_False()
Chain_verify_replace_block_expect_False()
Chain_verify_change_block_expect_False()
Chain_verify_no_blocks_added_expect_True()
