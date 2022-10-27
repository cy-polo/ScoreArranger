from music_manager import generate_chord

# get the note
note = input("Enter a note: ")
# get the chord type
chord_type = input("Enter a chord type: ")
# get the chord
chord = generate_chord(note, chord_type)
# print the chord
print(chord)