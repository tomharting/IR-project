import os
import midi

rootdir = 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/clean_midi'
nameDir = {}
medFiles = []

def extractTrackName(filename):
    trackNames = []
    events = []

    try:
        pattern = midi.read_midifile(filename)
        for track in pattern:
            for event in track:
                events.append(event)

        for event in events:
            if event is not None:

                if isinstance(event, midi.events.TrackNameEvent):
                    if hasattr(event, "text"):
                        # trackNames.append(event.text.lower())
                        if event.text.lower().__eq__('melody'):
                            medFiles.append(fileName)
                            print(fileName)

    except TypeError:
        print "type error"
    except IOError:
        print "IO error"
    except:
        print "unkown error"

    return trackNames


def addNamesToDir(trackNames):
    for name in trackNames:
        if name not in nameDir:
            nameDir[name] = 1
        else:
            nameDir[name] += 1


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        fileName = os.path.join(subdir, file)
        if fileName.endswith(".mid"):
            names = extractTrackName(fileName)
            addNamesToDir(names)

print repr(nameDir)
print repr(medFiles)
