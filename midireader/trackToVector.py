import os
import midi
import json
import findTrackNames

# Converts Lakh OR miret midi files to a tick vector (vector of time differences)
# Next converts a tick vector to a IOI vector

ROOT_DIR = 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/Git/'
ALL_KALH_TARGET_TEST_SONG_NAMES_PATH = 'Lakh/lakh_target_midi_songs_test_set_100.txt'
TARGET_VECTOR_MAP_KAHL_INNER_PATH = 'comparer/data/targetVectorMapLakh.json'

def getTrackTicksLakh(filename):
    pattern = midi.read_midifile(filename)
    ticks = []
    for track in pattern:
        melTrack = False
        tmpSum = 0;
        for event in track:
            if isinstance(event, midi.events.TrackNameEvent):
                if hasattr(event, "text"):
                    if event.text.lower().__eq__('melody'):
                        melTrack = True
            if melTrack:
                if isinstance(event, midi.events.NoteOnEvent):
                    ticks.append(event.tick+tmpSum)
                    tmpSum = 0
                else:
                    tmpSum += event.tick
    return ticks

# contains only one track
def getTrackTicksMiret(filename):
    pattern = midi.read_midifile(filename)
    ticks = []
    for track in pattern:
        tmpSum = 0;
        for event in track:
                # OnNoteEvents with a velocity of zero are used for breaks between notes.
                if isinstance(event, midi.events.NoteOnEvent) and  event.data[1] is not 0:
                    ticks.append(event.tick+tmpSum)
                    tmpSum = 0
                else:
                    tmpSum += event.tick
    return ticks

def tickToIOI(tickList):
    ratio = []
    if tickList:
        ratio = [1.0]
        tickList.pop(0)
        ticksClean = list(filter(lambda a: a != 0, tickList))
        for i in range(1, len(ticksClean)):
            rat = float(ticksClean[i])/float(ticksClean[i-1])
            ratio.append(rat)

    return ratio


def getAllSongFileName(fname):
    with open(fname) as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
    return content

def getTrackRatioMiret(fname):
    ticks = getTrackTicksMiret(fname)
    return tickToIOI(ticks)

def getTrackRatioLakh(fname):
    ticks = getTrackTicksLakh(fname)
    return tickToIOI(ticks)

def createKahlTestSet():
    song_ratio = {}
    all_melody_files = getAllSongFileName(ROOT_DIR + ALL_KALH_TARGET_TEST_SONG_NAMES_PATH)

    for file in all_melody_files:
        fileName = os.path.join(findTrackNames.ROOT_DIR, file)
        final = getTrackRatioLakh(fileName)
        if final:
            song_ratio[fileName] = final

    with open(ROOT_DIR + TARGET_VECTOR_MAP_KAHL_INNER_PATH, 'w') as file:
        file.write(json.dumps(song_ratio))

