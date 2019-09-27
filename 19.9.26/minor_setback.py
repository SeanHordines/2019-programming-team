import math

pitches = []

for n in range(int(input())):
    freq = float(input())
    while(freq < 440.0):
        freq *= 2

    alpha = 12*math.log(freq/440.0)/math.log(2.0)
    alpha = int(alpha+.5)
    p = alpha % 12
    pitches.append(p)

keys = [
    [10, 0, 2, 3, 5, 7, 9],
    [3, 5, 7, 8, 10, 0, 2],
    [6, 8, 10, 11, 1, 3, 5],
    [9, 11, 0, 2, 4, 5, 7],
    [10, 0, 1, 3, 5, 6, 8]
]

names = ["G major", "C major", "Eb major", "F# major", "G minor"]

for pitch in pitches:
    i = 0
    for key in keys:
        if(pitch not in key):
            names[i] = ""
        i += 1

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

names = set(names)
if(len(names) == 2):
    names = list(names)
    names.remove("")
    key = names[0]
    print(key)
    for pitch in pitches:
        note = notes[pitch]
        if(len(note) > 1) and ((key == "Eb major") or (key == "G minor")):
            note = notes[pitch+1] + "b"
        print(note)

else:
    print("cannot determine key")
