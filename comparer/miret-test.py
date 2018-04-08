import json
import os
import saa
import operator
import sys
import numpy as np
sys.path.append('../')
sys.path.insert(0, 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/Git/midi-reader')

import trackToVector
import calculateMetrics

rootdir = 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/Git/'
allTargetSongFileLocation = 'QBT/REFMIDI/'
allRecordedSongFileLocation = 'QBT/onset/'
allRecordToTargetSongFileName = 'QBT/query.list.txt'

def getFileContent (fname):
    fileName = os.path.join(rootdir, fname)
    with open(fileName) as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
    return content

def createIndexFiles():
    mappings = getFileContent(allRecordToTargetSongFileName)

    queryTargetMap = {}
    targetVectorMap = {}
    queryVectorMap = {}
    queryFiles = set()
    targetFiles = set()
    for map in mappings:
        [query, target] = map.split(' ')
        query_file = allRecordedSongFileLocation + query.replace('.wav', '.onset')
        target_file = allTargetSongFileLocation + target+'.mid'

        queryFiles.add(query_file)
        targetFiles.add(target_file)

        queryTargetMap[query_file] = target_file

    for query in queryFiles:
        # TODO: Check correct format of onset file
        queryVectorMap[query] = getFileContent(query)[0].split()

    for target in targetFiles:
        targetVectorMap[target] = trackToVector.getTrackRatioMiret(rootdir + target)

    with open('data/queryVectorMapMiret.json', 'w') as file:
        file.write(json.dumps(queryVectorMap))
    with open('data/targetVectorMapMiret.json', 'w') as file:
        file.write(json.dumps(targetVectorMap))
    with open('data/queryTargetMapMiret.json', 'w') as file:
        file.write(json.dumps(queryTargetMap))


def testAllMiret():
    finalRes = {}
    fileBase = rootdir + 'comparer/data'
    queryVectorMap = json.load(open(fileBase + 'queryVectorMapMiret.json'))
    targetVectorMap = json.load(open(fileBase +'targetVectorMapMiret.json'))
    queryTargetMap = json.load(open(fileBase +'queryTargetMapMiret.json'))

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

def testCombination():
    finalRes = {}
    fileBase = rootdir + 'comparer/data'
    queryVectorMap = json.load(open(fileBase + 'queryVectorMap.json'))
    targetVectorMap = json.load(open(fileBase + 'targetVectorMap.json'))
    queryTargetMap = json.load(open(fileBase + 'queryTargetMap.json'))
    query = 'QBT/onset/0287.onset'
    target = 'QBT/REFMIDI/0033.mid'
    query_ioi = np.array(queryVectorMap[query]).astype(np.float)
    target_ioi = np.array(targetVectorMap[target])
    result = saa.compareTracks(query_ioi, target_ioi)


# createIndexFiles()
topTen, reciprocal = testAllMiret()
print topTen, reciprocal
# testCombination()