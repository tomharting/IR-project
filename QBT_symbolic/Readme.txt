************************************************
Query-by-Tapping symbolic corpus for MIREX 2009
************************************************

Author: 
Shu-Jen Show Hsiao (show.cs95g@nctu.edu.tw)
Description: 
This Corpus contains 143 ground-truth monophonic MIDI files and 410 symbolic onset query files.
These onset files are collected from web site http://210.68.135.13/ki/donate.asp
The web page will prompt a MIDI file randomly then user can tap the rhythm from beginning by keyboard space bar.

Directory and files:
./Midi		<DIR> MIDI files, The file name is xxxx.mid where 'xxxx' is midi ID.
./Onset Query	<DIR> Query files, The file name is yyyy.onset where 'yyyy' is onset ID.
		These files recorded the onset time (in ms) of users' tapping, where the first onset time is always 0.
./answer.txt	<File> This file describes the query onset files with MIDI ground-truth.  
 