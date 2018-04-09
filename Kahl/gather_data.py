import csv
import sys
sys.path.insert(0, 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/Git/keyboard-reader')
import listener
import json

ALL_SONG_ID_FILE = 'all_song_to_id.csv'
SAVE_TAP_PATH = 'all_user_query/'
QUERY_TARGET_MAP_FILE_NAME = 'queryTargetMapLakh.csv'

def read_song_id():
    with open(ALL_SONG_ID_FILE, mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]: rows[1] for rows in reader}
    return mydict


def save_vector_to_file(vector, tester_name, song_name, num_record):
    # save targetVectorMap + queryTargetMap
    with open(SAVE_TAP_PATH + tester_name + str(num_record) +'.onset', 'w') as file:
        file.write(' '.join(map(str, vector)))
    with open(QUERY_TARGET_MAP_FILE_NAME, "a") as file:
        file.write(tester_name + str(num_record) +'.onset' + ' ; ' + song_name + '\n')


def choose_song(song_id_map, tester_name, num_record):
    song_id = raw_input("Which song are you going to tap? (provide song-id): ")
    correct_song = raw_input('Song you are tapping: ' + song_id_map[song_id] + '; Is this correct? (1 = yes, 0=no) ')
    if correct_song == '0':
        return num_record, True
    print 'Oke, good luck! You can tap now by using space-bar, when your finished press the shift on the right side'
    vector = listener.record_tapping()
    save_vector_to_file(vector, tester_name, song_id_map[song_id], num_record)

    tab_another_song_check = raw_input("Tap another song? (1 = yes, 0 = no): ")
    if tab_another_song_check == '0':
        return num_record, False
    return num_record+1, True


def do_test(song_id_map):
    tab_another_song = True
    tester_name = raw_input("What's your name (id) ?: ")
    num_record = 1
    while tab_another_song:
        num_record, tab_another_song = choose_song(song_id_map, tester_name, num_record)


    print "Thank you " + tester_name + " for your time and participation in our research!"


song_id_map = read_song_id()
print song_id_map
do_test(song_id_map)
