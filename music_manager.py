NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
CHORDS = {
    "major": [0, 4, 7],
    "minor": [0, 3, 7],
    "diminished": [0, 3, 6],
    "augmented": [0, 4, 8]
}

# function to generate a chord from a note
def generate_chord(note, chord_type, octave=0):
    global NOTES, CHORDS

    # get the index of the note in the list
    note_index = NOTES.index(note)
    # get the chord type
    chord_type = CHORDS[chord_type]
    # get the chord
    chord = [NOTES[(note_index + chord_type[i]) % 12] for i in range(len(chord_type))]

    # change the octave of the chord

    print("accord : ", chord)

    if octave != 0:
        # Note de basse toujours 3

        for note in range(len(chord)):
            if note == 0:
                chord[note] += str(octave)
            else:
                chord[note] += str(octave + 1)


        '''if position_2nd_note > position_3rd_note:
            chord[1] += str(octave + 1)
            chord[2] += str(octave)'''

    # return the chord
    # [x.lower() for x in chord] => Convert to lowercase
    return chord

# Get the range of note
def get_note_range(note):
    global NOTES

    # get the index of the note in the list
    note_index = NOTES.index(note)
    # get the range
    note_range = [NOTES[(note_index + i) % 12] for i in range(12)]
    # return the range
    return note_range

# Change octave of the note
def change_octave(note, octave):
    if octave == 0:
        return note
    elif octave > 0:
        return note + str(octave)
    else:
        return note - str(octave)


# Generate the next logical chord
def generate_next_chord(note, chord_type, octave=0):
    global NOTES, CHORDS

    # get the index of the note in the list
    note_index = NOTES.index(note)
    # get the chord type
    chord_type = CHORDS[chord_type]
    # get the chord
    chord = [NOTES[(note_index + chord_type[i]) % 12] for i in range(len(chord_type))]

    # change the octave of the chord
    if octave != 0:
        # Note de basse toujours 3

        for note in range(len(chord)):
            if note == 0:
                chord[note] += str(octave)
            else:
                chord[note] += str(octave + 1)

    # return the chord
    # [x.lower() for x in chord] => Convert to lowercase
    return chord
