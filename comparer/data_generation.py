import os
import sys
import json
sys.path.append('../')
sys.path.insert(0, 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/Git/midi-reader')

import trackToVector

ROOT_DIR = 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/Git/'
JSON = '.json'
QUERY_TARGET_MAP = 'queryTargetMap'
QUERY_VECTOR_MAP = 'queryVectorMap'
TARGET_VECTOR_MAP = 'targetVectorMap'
DATA_PATH = 'comparer/data/'

def getFileContent (inner_file_path):
    file_path = os.path.join(ROOT_DIR, inner_file_path)
    with open(file_path) as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
    return content

# Needs the inner paths to the test files, target files and mapping between test-queries and targets.
# Creates 3 data files with dictionaries in DATA containing IOI vectors, which can be used as input for metric calculation
def createIndexFiles(test_set_name, query_test_location, target_test_location, mapping_location):
    query_file_location = ROOT_DIR + query_test_location
    target_file_location = ROOT_DIR + target_test_location

    mappings = getFileContent(ROOT_DIR + mapping_location)

    query_target_map = {}
    targetVectorMap = {}
    queryVectorMap = {}
    queryFiles = set()
    targetFiles = set()
    for map in mappings:
        [query, target] = map.split(' ')
        # TODO make seperate file ending for different test sets
        query_file = query_file_location + query.replace('.wav', '.onset')
        target_file = target_file_location + target+'.mid'

        queryFiles.add(query_file)
        targetFiles.add(target_file)

        query_target_map[query_file] = target_file

    for query in queryFiles:
        # TODO: Check correct format of onset file (Does it need to be normalized?)
        queryVectorMap[query] = getFileContent(query)[0].split()

    for target in targetFiles:
        targetVectorMap[target] = trackToVector.getTrackRatioMiret(target)

    query_path = ROOT_DIR + DATA_PATH + QUERY_VECTOR_MAP + test_set_name + JSON
    target_path = ROOT_DIR + DATA_PATH + TARGET_VECTOR_MAP + test_set_name + JSON
    query_target_map_path = ROOT_DIR  + DATA_PATH + QUERY_TARGET_MAP + test_set_name + JSON

    with open(query_path, 'w') as file:
        file.write(json.dumps(queryVectorMap))
    with open(target_path, 'w') as file:
        file.write(json.dumps(targetVectorMap))
    with open(query_target_map_path, 'w') as file:
        file.write(json.dumps(query_target_map))