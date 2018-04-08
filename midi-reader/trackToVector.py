import os
import midi
import json

rootdir = 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/clean_midi'
songNameFile = '100popSongs.txt'
songratio = {}

def getTrackTicksLakh(filename):
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

def getTrackRatioMiret(fname):
    ticks = getTrackTicksMiret(fname)
    return tickToRatio(ticks)

def getTrackRatioLakh(fname):
    ticks = getTrackTicksLakh(fname)
    return tickToRatio(ticks)

def createKahlTestSet():
    medFiles = getAllSongFileName(songNameFile)

    for file in medFiles:
        fileName = os.path.join(rootdir, file)
        final = getTrackRatioLakh(fileName)
        if final:
            songratio[file] = final

    with open('./comparer/data/targetVectorMapLakh.json', 'w') as file:
        file.write(json.dumps(songratio))