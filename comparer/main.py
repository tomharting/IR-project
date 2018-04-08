import data_generation
import runTest

MIRET = 'Miret'
LAKH = 'Lakh'
TEST_LAKH_QUERY_INNER_PATH= 'keyboard-reader/lakh-tap-test'
TEST_LAKH_TARGET_INNER_PATH= 'midi-reader/??'
TEST_LAKH_QUERY_TARGET_INNER_PATH= '??'
TEST_MIRET_TARGET_INNER_PATH = 'QBT/REFMIDI/'
TEST_MIRET_QUERY_INNER_PATH = 'QBT/onset/'
TEST_MIRET_QUERY_TARGET_INNER_PATH = 'QBT/query.list.txt'

def genDataFiles():
    data_generation.createIndexFiles(MIRET, TEST_MIRET_QUERY_INNER_PATH, TEST_MIRET_TARGET_INNER_PATH, TEST_MIRET_QUERY_TARGET_INNER_PATH)
    # data_generation.createIndexFiles(LAKH)

def testToRun():
    # runTest.execute(MIRET)
    a = runTest.testCombination(MIRET)
    print a

genDataFiles()
res = testToRun()
print res