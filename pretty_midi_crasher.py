import os, sys, shutil
import pretty_midi

# Name directory to crawl. Cannot contain subdirectories.
songs_directory = "data/test_cases/"
if "--location" in sys.argv: # command line option to choose folder to filter
	songs_directory = sys.argv[sys.argv.index("--location") + 1]
if songs_directory[-1] != "/":
	songs_directory += "/"

# Name directory to place bad files in.
bad_files_directory = "removed/" + songs_directory
if "--dump" in sys.argv: # command line option to choose place to leave bad MIDIs
	bad_files_directory = sys.argv[sys.argv.index("--dump") + 1]

# Ensure dump directory exists
bad_files_directory_path_components = bad_files_directory.split("/")
validated_path = ""
for dir in bad_files_directory_path_components:
	try:
		os.listdir(validated_path + dir)
	except OSError as e:
		os.mkdir(validated_path + dir)
	finally:
		validated_path += dir + "/"

sample_songs = [
	"2_ase.mid",
	"Carulli_Concerto_Flauto_Chitarra_Orchestra_Allegro.mid"
]

# midi_data = pretty_midi.PrettyMIDI("data/classical/2_ase.mid")
# midi_data = pretty_midi.PrettyMIDI("data/classical/Carulli_Concerto_Flauto_Chitarra_Orchestra_Allegro.mid")

# Open file for log of files removed.
bad_files_log = open("removed_files.csv", "w")

for song in os.listdir(songs_directory):
	try:
		midi_data = pretty_midi.PrettyMIDI(songs_directory + song)
	except IOError as e:
		print "Failed to import " + song
		bad_files_log.write(song + "\n")
		shutil.move(songs_directory + song, bad_files_directory + song)
	else:
		print "Succeeded in importing " + song
	
bad_files_log.close()