import json
import data_generation
import numpy as np
import saa
import calculateMetrics

def execute(test_set_name):
    finalRes = {}
    fileBase = data_generation.ROOT_DIR + data_generation.DATA_PATH
    query_path = data_generation.QUERY_VECTOR_MAP + test_set_name + data_generation.JSON
    target_path = data_generation.TARGET_VECTOR_MAP + test_set_name + data_generation.JSON
    query_target_map_path = data_generation.QUERY_TARGET_MAP + test_set_name + data_generation.JSON
    queryVectorMap = json.load(open(fileBase + query_path))
    targetVectorMap = json.load(open(fileBase + target_path))
    queryTargetMap = json.load(open(fileBase + query_target_map_path))

    for query in queryTargetMap:
        print query
        resultMap = {}
        for target in targetVectorMap:
            print target
            query_ioi = np.array(queryVectorMap[query]).astype(np.float)
            target_ioi = np.array(targetVectorMap[target])
            resultMap[target] = saa.compareTracks(query_ioi, target_ioi)

        finalRes[query] = resultMap
        break
    return calculateMetrics.calcMetrics(finalRes, queryTargetMap)

def testCombination(test_set_name):
    fileBase = data_generation.ROOT_DIR + data_generation.DATA_PATH
    query_path = data_generation.QUERY_VECTOR_MAP + test_set_name + data_generation.JSON
    target_path = data_generation.TARGET_VECTOR_MAP + test_set_name + data_generation.JSON
    query_target_map_path = data_generation.QUERY_TARGET_MAP + test_set_name + data_generation.JSON
    queryVectorMap = json.load(open(fileBase + query_path))
    targetVectorMap = json.load(open(fileBase + target_path))
    query = data_generation.ROOT_DIR + 'QBT/onset/0287.onset'
    target = data_generation.ROOT_DIR +  'QBT/REFMIDI/0033.mid'
    query_ioi = np.array(queryVectorMap[query]).astype(np.float)
    target_ioi = np.array(targetVectorMap[target])
    result = saa.compareTracks(query_ioi, target_ioi)
    return result