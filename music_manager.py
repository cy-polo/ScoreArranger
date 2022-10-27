NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
CHORDS = {
    "major": [0, 4, 7],
    "minor": [0, 3, 7],
    "diminished": [0, 3, 6],
    "augmented": [0, 4, 8]
}

# function to generate a chord from a note
def generate_chord(note, chord_type):
    global NOTES, CHORDS

    # get the index of the note in the list
    note_index = NOTES.index(note)
    # get the chord type
    chord_type = CHORDS[chord_type]
    # get the chord
    chord = [NOTES[(note_index + chord_type[i]) % 12] for i in range(len(chord_type))]
    # return the chord
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

# Numbering of the notes
def get_note_number(range, note):
    return False