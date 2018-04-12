import data_generation
import runTest
import datetime
import os

MIRET = 'Miret'
LAKH = 'Lakh'
QBTS = 'QBTS'
QBTS_SMALL = 'QBTS_SMALL'
MIR_QBTS = 'MIR_QBT'

TEST_LAKH_QUERY_INNER_PATH= 'Lakh/all_user_query/'
TEST_LAKH_TARGET_FULL_PATH= 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/clean_midi/'
TEST_LAKH_QUERY_TARGET_INNER_PATH= 'Lakh/queryTargetMapLakh.csv'

TEST_MIRET_TARGET_INNER_PATH = 'QBT/REFMIDI/'
TEST_MIRET_QUERY_INNER_PATH = 'QBT/onset/'
TEST_MIRET_QUERY_TARGET_INNER_PATH = 'QBT/query.list.txt'


TEST_MIR_QBT_TARGET_INNER_PATH = 'MIR-QBT/midi/'
TEST_MIR_QBT_QUERY_INNER_PATH = 'MIR-QBT/query/'
TEST_MIR_QBT_QUERY_TARGET_INNER_PATH = 'MIR-QBT/queryOnset.list'


TEST_QBTS_TARGET_INNER_PATH = 'QBT_symbolic/Midi/'
TEST_QBTS_QUERY_INNER_PATH = 'QBT_symbolic/Onset query/'
TEST_QBTS_QUERY_TARGET_INNER_PATH = 'QBT_symbolic/answer.txt'

TEST_QBTS_SMALL_TARGET_INNER_PATH = 'QBT_symbolic/Midi/'
TEST_QBTS_SMALL_QUERY_INNER_PATH = 'QBT_symbolic/Onset query/'
TEST_QBTS_SMALL_QUERY_TARGET_INNER_PATH = 'QBT_symbolic/answer_100.txt'

TEST_TEST_MIRET_QUERY_TARGET_INNER_PATH = 'QBt/test_query_list.txt'

def genDataFiles():
    # data_generation.createIndexFiles(MIRET, TEST_MIRET_QUERY_INNER_PATH, TEST_MIRET_TARGET_INNER_PATH, TEST_MIRET_QUERY_TARGET_INNER_PATH)
    # data_generation.createIndexFilesQBTS(QBTS, TEST_QBTS_QUERY_INNER_PATH, TEST_QBTS_TARGET_INNER_PATH, TEST_QBTS_QUERY_TARGET_INNER_PATH)
    # data_generation.createIndexFilesQBTS(MIR_QBTS, TEST_MIR_QBT_QUERY_INNER_PATH, TEST_MIR_QBT_TARGET_INNER_PATH,TEST_MIR_QBT_QUERY_TARGET_INNER_PATH)

    # data_generation.createIndexFiles(MIRET, TEST_MIRET_QUERY_INNER_PATH, TEST_MIRET_TARGET_INNER_PATH, TEST_TEST_MIRET_QUERY_TARGET_INNER_PATH)
    data_generation.createLakhFiles(LAKH, TEST_LAKH_QUERY_INNER_PATH, TEST_LAKH_TARGET_FULL_PATH, TEST_LAKH_QUERY_TARGET_INNER_PATH)
    # data_generation.createIndexFilesQBTS(QBTS_SMALL, TEST_QBTS_SMALL_QUERY_INNER_PATH, TEST_QBTS_SMALL_TARGET_INNER_PATH, TEST_QBTS_SMALL_QUERY_TARGET_INNER_PATH)

def testToRun(penalty_i, penalty_d):

    topTen, reciprocal = runTest.execute(QBTS, penalty_i, penalty_d)
    print topTen, reciprocal

def runCaclMetricFile(penalty_i, penalty_d):
    topTen, reciprocal = runTest.executePreRunData(QBTS,  penalty_i, penalty_d)
    print topTen, reciprocal



# TODO: save the resulting scores, to check metric calculation
penalty_i = 3
penalty_d = 2
# genDataFiles()
# print datetime.datetime.now()
res = testToRun(penalty_i, penalty_d)
# print datetime.datetime.now()
# runCaclMetricFile(penalty_i, penalty_d)
