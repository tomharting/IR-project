import data_generation
import runTest
import datetime

MIRET = 'Miret'
LAKH = 'Lakh'
QBTS = 'QBTS'
QBTS_SMALL = 'QBTS_SMALL'

TEST_LAKH_QUERY_INNER_PATH= 'Lakh/all_user_query/'
TEST_LAKH_TARGET_FULL_PATH= 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/clean_midi/'
TEST_LAKH_QUERY_TARGET_INNER_PATH= 'Lakh/queryTargetMapLakh.csv'

TEST_MIRET_TARGET_INNER_PATH = 'QBT/REFMIDI/'
TEST_MIRET_QUERY_INNER_PATH = 'QBT/onset/'
TEST_MIRET_QUERY_TARGET_INNER_PATH = 'QBT/query.list.txt'

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
    # data_generation.createIndexFiles(MIRET, TEST_MIRET_QUERY_INNER_PATH, TEST_MIRET_TARGET_INNER_PATH, TEST_TEST_MIRET_QUERY_TARGET_INNER_PATH)
    # data_generation.createLakhFiles(LAKH, TEST_LAKH_QUERY_INNER_PATH, TEST_LAKH_TARGET_FULL_PATH, TEST_LAKH_QUERY_TARGET_INNER_PATH)
    data_generation.createIndexFilesQBTS(QBTS_SMALL, TEST_QBTS_SMALL_QUERY_INNER_PATH, TEST_QBTS_SMALL_TARGET_INNER_PATH, TEST_QBTS_SMALL_QUERY_TARGET_INNER_PATH)

def testToRun(penalty_i, penalty_d):

    topTen, reciprocal = runTest.execute(QBTS_SMALL, penalty_i, penalty_d)
    print topTen, reciprocal

def runCaclMetricFile(penalty_i, penalty_d):
    topTen, reciprocal = runTest.executePreRunData(QBTS_SMALL,  penalty_i, penalty_d)
    print topTen, reciprocal



# TODO: save the resulting scores, to check metric calculation
penalty_i = 5
penalty_d = 5
# genDataFiles()
# print datetime.datetime.now()
res = testToRun(penalty_i, penalty_d)
# print datetime.datetime.now()
# runCaclMetricFile(penalty_i, penalty_d)