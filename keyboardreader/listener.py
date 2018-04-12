from pynput import keyboard
import time
import numpy as np

prevTime = 0
prevDuration = 0
timeVector = np.array([])

def on_press(key):
    global prevDuration
    global prevTime
    global timeVector

    currentTime = time.time()

    if prevTime != 0:
        prevDuration = currentTime - prevTime
        timeVector = np.append(timeVector, prevDuration)

    prevTime = currentTime

    if key == keyboard.Key.shift_r:
        # Stop listener
        return False


# Collect events until released
def record_tapping():
    global timeVector
    print timeVector

    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()

    timeVector = timeVector[:-1]

    featureVector = np.array([1])
    for i in range(1, len(timeVector)):
        feature = timeVector[i]/timeVector[i-1]
        featureVector = np.append(featureVector, feature)

    return featureVector.tolist()
