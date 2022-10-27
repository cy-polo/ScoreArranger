from pymusicxml import *
from music_manager import generate_chord, get_note_number
from random import choice

# print(get_note_number("C", "E"))

score = Score(title="Algorithmically Generated MusicXML", composer="ScoreArranger")
part = Part("Piano")
score.append(part)

pitch_bank = ["C", "G", "F"]
possibilities = []

for i in pitch_bank:
    accords = generate_chord(i, "major")
    possibilities.append(accords)

measures = []

# Pour 20 mesures
for i in range(20):
    # 1ère mesure en 3/4, pas de changement pour les autres
    m = Measure(time_signature=(3, 4) if i == 0 else None, barline="end" if i == 19 else None)

    for beat in range(3):
        # Choisir une note au hasard dans la liste des possibilités
        chord = choice(possibilities)
        # Ajouter la note à la mesure
        m.append(BeamedGroup([ Chord(chord, 1.0) ]))

    measures.append(m)

part.extend(measures)

score.export_to_file("Main.musicxml")




'''
    # Créer 3 temps dans la mesure
    for beat_num in range(3):
        if (i + beat_num) % 3 == 0:
            # one quarter note triad
            m.append(Chord(choices(possibilities, k=3), 1.0))
        elif (i + beat_num) % 3 == 1:
            # two eighth note dyads
            m.append(BeamedGroup([Chord(choices(possibilities, k=2), 0.5) for _ in range(2)]))
        else:
            # four 16th note notes
            m.append(BeamedGroup([Note(choice(possibilities), 0.25) for _ in range(4)]))
    measures.append(m)
'''