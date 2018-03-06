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

    print 'Tap!'

    currentTime = time.time()

    if prevTime != 0:
        prevDuration = currentTime - prevTime
        timeVector = np.append(timeVector, prevDuration)
        print(timeVector)

    prevTime = currentTime

    if key == keyboard.Key.shift_r:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()