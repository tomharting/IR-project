import midi

def getTrack(data, trackNum):
    events = []
    for track in data:
        for event in track:
            events.append(event)

    for event in events:
        if event is not None:
            if hasattr(event, "channel"):
                if event.channel != trackNum:
                    events.remove(event)

    return events


midifile = "songs/Sharp Dressed Man.mid"
pattern = midi.read_midifile(midifile)
# trackData = getTrack(pattern, 4)

# print(repr(trackData))
print repr(pattern)
