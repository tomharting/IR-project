import operator

# Calculates the metrics based on a score file

# Wants dictionary: query_file : [target_file : score]
def calculate_all_metric(dic_scores, dic_query_to_target):
    topTen = 0.
    reciprocal = 0.
    for query in dic_scores:
        target = dic_query_to_target[query].encode('UTF8').replace('\\', '/')
        targets_sorted_by_score = sorted(dic_scores[query].items(), key=operator.itemgetter(1))
        target_names_sorted = zip(*targets_sorted_by_score)[0]
        target_names_formatted = [x.encode('UTF8').replace('\\', '/') for x in target_names_sorted]
        if target in target_names_formatted[:10]:
            topTen += 1.
        reciprocal += 1./(target_names_formatted.index(target) + 1)
    return [topTen, reciprocal]
