from pymusicxml import *
from music_manager import generate_chord
from random import choice

NOTES_RANGE = ["C0", "C#0", "D0", "D#0", "E0", "F0", "F#0", "G0", "G#0", "A0", "A#0", "B0", "C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1", "G#1", "A1", "A#1", "B1", "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6", "D#6", "E6", "F6", "F#6", "G6", "G#6", "A6", "A#6", "B6", "C7", "C#7", "D7", "D#7", "E7", "F7", "F#7", "G7", "G#7", "A7", "A#7", "B7", "C8", "C#8", "D8", "D#8", "E8", "F8", "F#8", "G8", "G#8", "A8", "A#8", "B8"]

score = Score(title="Algorithmically Generated MusicXML", composer="ScoreArranger")
part_key_G = Part("Piano")
part_key_F = Part("Piano")

# Link piano part to score
score.append(PartGroup([part_key_G, part_key_F]))

pitch_bank = ["C", "G", "F"]

possibilities = []

for i in pitch_bank:
    accords = generate_chord(i, "major", 3)
    if NOTES_RANGE.index(accords[1]) > NOTES_RANGE.index(accords[2]):
        print(accords[1][:-1:], accords[2][:-1:])

        accord_2 = accords[1][:-1:] + str(4)
        accord_3 = accords[2][:-1:] + str(5)

        print(accord_2, accord_3)

        possibilities.append([accords[0], accord_2, accord_3])
    else:
        possibilities.append(accords)

print("Possibilities", possibilities)

measures_G = []
measures_F = []

# For 20 measures
for i in range(20):
    # 1st measure in 3/4, no change for the others
    # Initialize measures in treble and bass clef
    G_m = Measure(time_signature=(3, 4) if i == 0 else None, barline="end" if i == 19 else None)
    F_m = Measure(clef="bass" if i == 0 else None, time_signature=(3, 4) if i == 0 else None, barline="end" if i == 19 else None)

    # Generate a random chord
    chord = choice(possibilities)

    content_G = []
    content_F = []

    print("Choice :", chord)

    for time in range(3):
        if time == 0:
            # Half note for the first beat, ground state
            content_G.append(Rest(1.0))
            content_F.append(Note(chord[0], 3.0))
        else:
            # Silence 1st beat treble clef
            # Chords for the other two beats in the treble clef
            print("Slice :", chord[-2:])
            content_G.append(Chord(chord[-2:], 1.0))

    F_m.append(content_F)
    G_m.append(content_G)

    measures_F.append(F_m)
    measures_G.append(G_m)

part_key_G.extend(measures_G)
part_key_F.extend(measures_F)

score.export_to_file("main.musicxml")