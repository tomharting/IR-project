import json
import generate_compare_files
import numpy as np
import shifted_alignment_algorithm
import evaluate_score

# Compares all the queries to the targets and saves the dictionary with the scores
# Runs a dictionary of scores against the metrics

SAA_OUTPUT_PATH = 'SAA_data_files/saa_outcome_'


def create_dataset_saa_score_file(test_set_name, penalty_i, penalty_d):
    finalRes = {}
    fileBase = generate_compare_files.ROOT_DIR + generate_compare_files.DATA_PATH

    query_path = generate_compare_files.QUERY_VECTOR_MAP + test_set_name + generate_compare_files.JSON
    target_path = generate_compare_files.TARGET_VECTOR_MAP + test_set_name + generate_compare_files.JSON
    query_target_map_path = generate_compare_files.QUERY_TARGET_MAP + test_set_name + generate_compare_files.JSON

    queryVectorMap = json.load(open(fileBase + query_path))
    targetVectorMap = json.load(open(fileBase + target_path))
    queryTargetMap = json.load(open(fileBase + query_target_map_path))

    for query in queryTargetMap:
        resultMap = {}
        for target in targetVectorMap:
            query_ioi = np.array(queryVectorMap[query]).astype(np.float)
            target_ioi = np.array(targetVectorMap[target])
            if test_set_name == 'QBTS_SMALL' or test_set_name == 'QBTS' or test_set_name == 'MIR_QBT':
                if target_ioi.size > query_ioi.size + 5:
                    target_ioi = target_ioi[0:query_ioi.size+5]

            resultMap[target] = shifted_alignment_algorithm.compare_IOI_vectors(query_ioi, target_ioi, penalty_i, penalty_d)

        finalRes[query] = resultMap

    with open(SAA_OUTPUT_PATH + test_set_name + "_" + str(penalty_i) + '_' + str(penalty_d), 'w') as file:
        file.write(json.dumps(finalRes))


def calculate_dataset_metric_from_score_file(test_set_name, penalty_i, penalty_d):
    dic = json.load(open(SAA_OUTPUT_PATH+test_set_name+ "_" + str(penalty_i) + '_' + str(penalty_d)))
    query_target_map_path = generate_compare_files.ROOT_DIR + generate_compare_files.DATA_PATH + generate_compare_files.QUERY_TARGET_MAP + test_set_name + generate_compare_files.JSON
    with open(query_target_map_path) as data_file:
        queryTargetMap = json.load(data_file)
    return evaluate_score.calculate_all_metric(dic, queryTargetMap)