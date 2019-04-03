Remove invalid MIDI files from a directory to a designated dump directory.

Options:
```--location``` - relative path from working directory to directory containing files to filter
```--dump``` - relative path from working directory to directory where bad MIDIs should be dumped

Will output a list of bad files in working directory in `removed_files.csv`.

Example bash script
```
#!/bin/bash

python pretty_midi_crasher.py --location data/classical --dump removed/classical
python pretty_midi_crasher.py --location data/jazz --dump removed/jazz
```

Some final thoughts: This isn't pretty. I'm sure you can still find plenty of ways to crash it. However, it's simple, it's readable and it works.