import os
import midi
import json

rootdir = 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/clean_midi'
songNameFile = 'melSongs.txt'
songratio = {}

def getTrackTicks(filename):
    pattern = midi.read_midifile(filename)
    ticks = []
    for track in pattern:
        melTrack = False
        tmpSum = 0;
        for event in track:
            if isinstance(event, midi.events.TrackNameEvent):
                if hasattr(event, "text"):
                    # trackNames.append(event.text.lower())
                    if event.text.lower().__eq__('melody'):
                        melTrack = True
            if melTrack:
                if isinstance(event, midi.events.NoteOnEvent):
                    ticks.append(event.tick+tmpSum)
                    tmpSum = 0
                else:
                    tmpSum += event.tick
    return ticks

def tickToRatio(tickList):
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

medFiles = getAllSongFileName(songNameFile)
for file in medFiles:
    fileName = os.path.join(rootdir, file)
    ticks = getTrackTicks(fileName)
    final = tickToRatio(ticks)
    if final:
        songratio[file] = final

with open('melsongratio.txt', 'w') as file:
    file.write(json.dumps(songratio))