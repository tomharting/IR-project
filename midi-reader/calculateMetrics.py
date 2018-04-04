import saa
import trackToVector
import json

targetSongDataFileName = 'melsongratio.txt'
recordedSongDataFileName = 'melsongratio.txt'

# map: songs root -> ratio vector
targetSongs = json.loads(targetSongDataFileName)[0]
# map: index -> map: targetSong -> ratio vector
recordings = json.loads(targetSongDataFileName)[0]

for i in range(0, recordings):
    score_list = {}
    for j in range(0, targetSongs):
        score_list[targetSongs[j]] = saa.compareTracks(recordings[i][0], targetSongs[j])

    sorted_score_list = sorted(score_list)
    sorted_score_list.keys().index(recordings[i])
