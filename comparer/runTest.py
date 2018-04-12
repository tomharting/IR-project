import json
import data_generation
import numpy as np
import saa
import calculateMetrics

def execute(test_set_name, penalty_i, penalty_d):
    finalRes = {}
    fileBase = data_generation.ROOT_DIR + data_generation.DATA_PATH
    query_path = data_generation.QUERY_VECTOR_MAP + test_set_name + data_generation.JSON
    target_path = data_generation.TARGET_VECTOR_MAP + test_set_name + data_generation.JSON
    query_target_map_path = data_generation.QUERY_TARGET_MAP + test_set_name + data_generation.JSON
    queryVectorMap = json.load(open(fileBase + query_path))
    targetVectorMap = json.load(open(fileBase + target_path))
    queryTargetMap = json.load(open(fileBase + query_target_map_path))
    count_q_bigger_t = 0
    for query in queryTargetMap:
        # print query
        resultMap = {}
        for target in targetVectorMap:
            query_ioi = np.array(queryVectorMap[query]).astype(np.float)
            target_ioi = np.array(targetVectorMap[target])
            if test_set_name == 'QBTS_SMALL' or test_set_name == 'QBTS' or test_set_name == 'MIR_QBT':
                if target_ioi.size > query_ioi.size + 5:
                    target_ioi = target_ioi[0:query_ioi.size+5]
            val = saa.compareTracks(query_ioi, target_ioi, penalty_i, penalty_d)
            if val is not -1:
                resultMap[target] = val
            if query_ioi.size > target_ioi.size:
                count_q_bigger_t += 1
                # print query, target, resultMap[target]

        finalRes[query] = resultMap

    with open('SAA_data_files/saa_outcome_' + test_set_name + "_" + str(penalty_i) + '_' + str(penalty_d), 'w') as file:
        file.write(json.dumps(finalRes))
    print "Number of queries larger then a target = ", count_q_bigger_t

    return calculateMetrics.calcMetrics(finalRes, queryTargetMap)

def executePreRunData(test_set_name, penalty_i, penalty_d):
    dic = json.load(open('SAA_data_files/saa_outcome_'+test_set_name+ "_" + str(penalty_i) + '_' + str(penalty_d)))
    query_target_map_path = data_generation.ROOT_DIR + data_generation.DATA_PATH + data_generation.QUERY_TARGET_MAP + test_set_name + data_generation.JSON
    # print(query_target_map_path)
    with open(query_target_map_path) as data_file:
        queryTargetMap = json.load(data_file)
    # print 'first: ', queryTargetMap
    return calculateMetrics.calcMetrics(dic, queryTargetMap)