import operator

# Wants dictionary: query_file : [target_file : score]
def calcMetrics(dic_scores, dic_query_to_target):
    topTen = 0.
    reciprocal = 0.
    for query in dic_scores:
        target = dic_query_to_target[query]
        sorted_res = sorted(dic_scores[query].items(), key=operator.itemgetter(1))
        unzipped_tar = zip(*sorted_res)[0]
        test = [x.encode('UTF8') for x in unzipped_tar]
        test2 = [x.replace('\\', '/') for x in test]
        target2 = target.encode('UTF8').replace('\\', '/')
        if target2 in test2[:10]:
            topTen += 1.
        # else:
        #     print query, target2, test2.index(target2)
        index = test2.index(target2)
        reciprocal += 1./(index + 1)
    return [topTen, reciprocal]


def testFun():
    dic = {}
    dic['q1'] = {'t1': 2, 't2': 1, 't3': 0} #sorted: t3 - t2 -t1 -> q1 = 2
    dic['q2'] = {'t1': 1, 't2': 3, 't3': 2} #sorted: t1 - t3 - t2 -> q2 = 1
    dic['q3'] = {'t1': 4, 't2': 5, 't3': 6} #sorted: t2 - t1 -t3 -> q3 = 2
    qt = {'q1': 't2', 'q2': 't1', 'q3': 't3'}
    calcMetrics(dic, qt)

