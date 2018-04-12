import json
import os

ROOT_DIR = 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/Git/'


def getFileContent (inner_file_path):
    file_path = os.path.join(ROOT_DIR, inner_file_path)
    with open(file_path) as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]

    splitted = content[0] #.split(' ')
    # vector = []
    # for s in splitted:
    #     vector.__add__(float(s))
    return splitted

def getFilePath(id, counter):
    file_path = ROOT_DIR + 'Lakh/all_user_query/' + id + str(counter) + '.onset'
    if os.path.isfile(file_path):
        return file_path
    return 'no'

def filterId(id):
    counter = 1
    files = []
    check = True
    while check:
        file_res = getFilePath(id, counter)
        if file_res is 'no':
            check = False
        else:
            files.append(file_res)
            counter +=1

    for i in range(len(files)-1, 0, -1):
        current_query = getFileContent(files[i])
        prev_query = getFileContent(files[i-1])
        replaced = current_query.replace(prev_query,'')
        splitted = replaced.split(' ')
        splitted.pop(0)
        splitted.pop(0)
        splitted[0] = '1.'
        splitted = ' '.join(splitted)
        print splitted
        with open(files[i], 'w') as file:
          file.write(splitted)

# filterId('B')
filterId('C')
filterId('D')
filterId('E')
filterId('F')
filterId('G')
filterId('H')
filterId('I')
filterId('J')
filterId('K')
filterId('T')