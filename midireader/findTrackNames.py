import os
import midi

# Go through all the files in the lakh dataset and retrieve melody files

# FIll in your path to the lakh dataset
ROOT_DIR = 'C:/Users/daniel.DANIEL-PC/Documents/uni/Master/Information retrieval/group project/clean_midi'

melody_files = []

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
                        if event.text.lower().__eq__('melody'):
                            melody_files.append(filename)

    except TypeError:
        print "type error"
    except IOError:
        print "IO error"
    except:
        print "unkown error"

    return trackNames


def findTracks():
    for subdir, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            fileName = os.path.join(subdir, file)
            if fileName.endswith(".mid"):
                extractTrackName(fileName)

    print repr(melody_files)

findTracks()
