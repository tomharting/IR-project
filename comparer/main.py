import generate_compare_files
import comparer

# Main can do the following things:
# - create the data files needed for evaluation
# - run datafiles to create score data file
# - run score file to get metrics

MIRET = 'Miret'
LAKH = 'Lakh'
QBTS = 'QBTS'
QBTS_SMALL = 'QBTS_SMALL'
MIR_QBTS = 'MIR_QBT'

TEST_LAKH_QUERY_INNER_PATH= 'Lakh/all_user_query/'
TEST_LAKH_TARGET_FULL_PATH= 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/clean_midi/'
TEST_LAKH_QUERY_TARGET_INNER_PATH= 'Lakh/queryTargetMapLakh.csv'

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
    # data_generation.createIndexFilesQBTS(QBTS, TEST_QBTS_QUERY_INNER_PATH, TEST_QBTS_TARGET_INNER_PATH, TEST_QBTS_QUERY_TARGET_INNER_PATH)
    # data_generation.createIndexFilesQBTS(MIR_QBTS, TEST_MIR_QBT_QUERY_INNER_PATH, TEST_MIR_QBT_TARGET_INNER_PATH,TEST_MIR_QBT_QUERY_TARGET_INNER_PATH)
    generate_compare_files.createLakhFiles(LAKH, TEST_LAKH_QUERY_INNER_PATH, TEST_LAKH_TARGET_FULL_PATH, TEST_LAKH_QUERY_TARGET_INNER_PATH)
    # data_generation.createIndexFilesQBTS(QBTS_SMALL, TEST_QBTS_SMALL_QUERY_INNER_PATH, TEST_QBTS_SMALL_TARGET_INNER_PATH, TEST_QBTS_SMALL_QUERY_TARGET_INNER_PATH)

def test_dataset(dataset_to_run, penalty_i, penalty_d):
    comparer.create_dataset_saa_score_file(dataset_to_run, penalty_i, penalty_d)

def calculate_dataset_metrics(dataset_to_run, penalty_i, penalty_d):
    topTen, reciprocal = comparer.calculate_dataset_metric_from_score_file(dataset_to_run, penalty_i, penalty_d)
    print topTen, reciprocal


penalty_i = 3
penalty_d = 2
dataset_to_run = QBTS
# Only generate datafiles when we have new data; Manually comment out all lines except the data you want to generate
# genDataFiles()
# Only generate score data file when having new data, or change in algorithm
# test_dataset(dataset_to_run, penalty_i, penalty_d)
# Runs a score file to get the metrics
# calculate_dataset_metrics(dataset_to_run, penalty_i, penalty_d)
