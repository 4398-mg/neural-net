import os
import pretty_midi

songs_directory = "data/classical/"
sample_songs = [
	"2_ase.mid",
	"Carulli_Concerto_Flauto_Chitarra_Orchestra_Allegro.mid"
]

# midi_data = pretty_midi.PrettyMIDI("data/classical/2_ase.mid")
# midi_data = pretty_midi.PrettyMIDI("data/classical/Carulli_Concerto_Flauto_Chitarra_Orchestra_Allegro.mid")

for song in sample_songs:
	try:
		midi_data = pretty_midi.PrettyMIDI(songs_directory + song)
	except Exception as e:
		print "Failed to import " + song
	else:
		print "Succeeded in importing " + song
	