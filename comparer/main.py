import data_generation
import runTest
import datetime

MIRET = 'Miret'
LAKH = 'Lakh'
TEST_LAKH_QUERY_INNER_PATH= 'Lakh/all_user_query/'
TEST_LAKH_TARGET_FULL_PATH= 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/clean_midi/'
TEST_LAKH_QUERY_TARGET_INNER_PATH= 'Lakh/queryTargetMapLakh.csv'
TEST_MIRET_TARGET_INNER_PATH = 'QBT/REFMIDI/'
TEST_MIRET_QUERY_INNER_PATH = 'QBT/onset/'
TEST_MIRET_QUERY_TARGET_INNER_PATH = 'QBT/query.list.txt'
TEST_TEST_MIRET_QUERY_TARGET_INNER_PATH = 'QBt/test_query_list.txt'

def genDataFiles():
    data_generation.createIndexFiles(MIRET, TEST_MIRET_QUERY_INNER_PATH, TEST_MIRET_TARGET_INNER_PATH, TEST_MIRET_QUERY_TARGET_INNER_PATH)
    # data_generation.createIndexFiles(MIRET, TEST_MIRET_QUERY_INNER_PATH, TEST_MIRET_TARGET_INNER_PATH, TEST_TEST_MIRET_QUERY_TARGET_INNER_PATH)
    # data_generation.createLakhFiles(LAKH, TEST_LAKH_QUERY_INNER_PATH, TEST_LAKH_TARGET_FULL_PATH, TEST_LAKH_QUERY_TARGET_INNER_PATH)

def testToRun():
    topTen, reciprocal = runTest.execute(MIRET)
    print topTen, reciprocal

genDataFiles()
print datetime.datetime.now()
res = testToRun()
print datetime.datetime.now()
