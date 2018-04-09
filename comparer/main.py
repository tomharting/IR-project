import data_generation
import runTest
import datetime

MIRET = 'Miret'
LAKH = 'Lakh'
TEST_LAKH_QUERY_INNER_PATH= 'keyboardreader/lakh-tap-test'
TEST_LAKH_TARGET_INNER_PATH= 'midi-reader/??'
TEST_LAKH_QUERY_TARGET_INNER_PATH= '??'
TEST_MIRET_TARGET_INNER_PATH = 'QBT/REFMIDI/'
TEST_MIRET_QUERY_INNER_PATH = 'QBT/onset/'
TEST_MIRET_QUERY_TARGET_INNER_PATH = 'QBT/query.list.txt'
TEST_TEST_MIRET_QUERY_TARGET_INNER_PATH = 'QBt/test_query_list.txt'

def genDataFiles():
    # data_generation.createIndexFiles(MIRET, TEST_MIRET_QUERY_INNER_PATH, TEST_MIRET_TARGET_INNER_PATH, TEST_MIRET_QUERY_TARGET_INNER_PATH)
    data_generation.createIndexFiles(MIRET, TEST_MIRET_QUERY_INNER_PATH, TEST_MIRET_TARGET_INNER_PATH, TEST_TEST_MIRET_QUERY_TARGET_INNER_PATH)
    # data_generation.createIndexFiles(LAKH)

def testToRun():
    topTen, reciprocal = runTest.execute(MIRET)
    print topTen, reciprocal

genDataFiles()
print datetime.datetime.now()
res = testToRun()
print datetime.datetime.now()
